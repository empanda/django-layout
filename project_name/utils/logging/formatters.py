import logging
import json
import datetime
import uuid
import decimal
import traceback

from django.http import HttpRequest
from django.utils.timezone import is_aware


class ExtendedJSONEncoder(json.JSONEncoder):
    """
    A JSON encoder that understands more Python types, including:
      * datetime.datetime
      * datetime.date
      * datetime.time
      * decimal.Decimal
      * uuid.UUID
      * django.http.HttpRequest

    This is mostly copied from django.core.serializers.json.DjangoJSONEncoder.
    We don't subclass that because of a lot dependencies that cause problems
    during settings initialization.

    For Django HttpRequest objects it returns a dictionary containing the
    session key, the user id, the path, the method, any HTTP headers and the id
    of the request.
    """
    def default(self, o):
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r

        elif isinstance(o, datetime.date):
            return o.isoformat()

        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r

        elif isinstance(o, decimal.Decimal):
            return str(o)

        elif isinstance(o, uuid.UUID):
            return str(o)

        elif isinstance(o, HttpRequest):
            request = o
            r = {
                'session': getattr(getattr(request, 'session', None), '_session_key', None),
                'user': getattr(getattr(request, 'user', None), 'id', None),
                'path_info': request.path_info,
                'method': request.method,
                'id': getattr(request, 'id', None),
                'META': dict([(key, value)for key, value in request.META.iteritems() if key.startswith('HTTP_')]),
            }
            return r

        else:
            return super(ExtendedJSONEncoder, self).default(o)


class JSONFormatter(logging.Formatter):
    """
    Formats LogRecords to JSON.

    Instead of just dumping the entire LogRecord to JSON, first it moves all
    the keys into a nested dictionary based on the format argument. You can
    see the default layout below.

    Note that the `extra` key will contain all the data that is passed to the
    logger using the extra keyword parameter. For example:

    logger.debug('message', extra={'ip': '127.0.0.1'})
    """

    default_layout = {
        'logger': ['name', 'levelno', 'levelname'],
        'file': ['pathname', 'filename', 'module', 'lineno', 'funcName'],
        'time': ['created', 'asctime', 'relativeCreated'],
        'process': ['thread', 'threadName', 'process', 'processName'],
        'message': ['message', 'msg', 'args'],
        'extra': 'all the extra parameters will go here',
        'exception': 'filled with exception info when an exception occurs',
    }

    default_fields = set(['relativeCreated', 'process', 'module', 'funcName',
        'message', 'filename', 'levelno', 'processName', 'lineno', 'asctime',
        'msg', 'args', 'exc_text', 'name', 'thread', 'created', 'threadName',
        'msecs', 'pathname', 'exc_info', 'levelname'])

    def __init__(self, layout=None, json_encoder=ExtendedJSONEncoder):
        """
        You can specify two different options to custimize the final JSON
        output.

        layout - The layout of the final JSON object. You can reorganize this
            to meet your needs.

        json_encoder - The encoder class to use when converting objects into
            there JSON compatible counterparts. You can override this to allow
            for additional types to be stored in JSON.
        """
        self.layout = self.default_layout
        if layout:
            self.layout = layout

        self.json_encoder = json_encoder

    def process_extra(self, record):
        """
        Determines the difference between the default set of fields on a
        LogRecord and the actual set of keys. These additional fields are the
        `extra` fields for the LogRecord.
        """
        extra = {}
        extra_keys = set(record.__dict__.keys()).difference(self.default_fields)
        for key in extra_keys:
            extra[key] = getattr(record, key)
        return extra

    def process_exception(self, exc_info):
        """
        Returns a dictionary with all the exception info included.

        The traceback is rendered in a JSON friendly way.
        """
        return {
            'type': unicode(exc_info[0]),
            'value': unicode(exc_info[1]),
            'traceback': [{'filename': st[0], 'line_number': st[1], 'function_name': st[2], 'text': st[3]}
                            for st in traceback.extract_tb(exc_info[2])],
        }

    def fill_layout(self, record, layout):
        """
        Returns a dictionary of nested dictionaries with data from the
        LogRecord. It uses the layout dictionary defined in the format option
        as the as the template to follow.
        """
        final = {}
        for name, fields in layout.items():
            if name is 'extra':
                final['extra'] = self.process_extra(record)
                continue

            if name is 'exception':
                if record.exc_info:
                    final['exception'] = self.process_exception(record.exc_info)
                continue

            final[name] = {}
            for field in fields:
                final[name][field] = getattr(record, field)
        return final

    def formatDate(self, timestamp):
        """
        Format `asctime` into the standard ISO format.

        The datetime is in UTC by default thus the 'Z' at the end.
        """
        dt = datetime.datetime.utcfromtimestamp(timestamp)
        r = dt.isoformat() + 'Z'
        return r

    def format(self, record):
        """
        Add `message` and `asctime` to the LogRecord and then process the log
        message into a dictionary which is returned a string of JSON.
        """
        record.message = record.getMessage()
        record.asctime = self.formatDate(record.created)
        log_data = self.fill_layout(record, self.layout)
        return json.dumps(log_data, cls=self.json_encoder)
