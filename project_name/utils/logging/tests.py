from django.utils import unittest
import json
import decimal
import uuid

from .formatters import JSONFormatter, ExtendedJSONEncoder


class ExtendedJSONEncoderTests(unittest.TestCase):
    def test_supports_uuid_objects(self):
        """ExtendedJSONEncoder should return the string representation of a UUID."""
        eje = ExtendedJSONEncoder()
        id = uuid.uuid4()
        output = eje.default(id)
        self.assertEqual(output, str(id))

class JSONFormatterTests(unittest.TestCase):
    def test_out_is_valid_json(self):
        """JSONFormatter should output valid JSON."""
        formatter = JSONFormatter()
        output = formatter.format(FakeLogRecord())

        self.assertIsInstance(json.loads(output), dict)

    def test_basic_usage(self):
        """
        JSONFormatter should be able to handle a simple LogRecord and return JSON for it.
        """
        expected_output = {
            'extra': {'ip': '127.0.0.1', 'foo': 'asfd'},
            'process': {'process': 7821, 'processName': 'MainProcess', 'threadName': 'MainThread', 'thread': 140735211397504},
            'file': {'funcName': 'main', 'pathname': 'test.py', 'lineno': 116, 'module': 'test', 'filename': 'test.py'},
            'time': {'relativeCreated': 8.126974105834961, 'asctime': '2012-11-20T23:30:59.111096Z', 'created': 1353454259.111096},
            'logger': {'levelno': 10, 'name': 'main', 'levelname': 'DEBUG'},
            'message': {'msg': 'in main function %s', 'message': "in main function ['foo']", 'args': ['foo']}
        }

        formatter = JSONFormatter()
        output_json = formatter.format(FakeLogRecord())
        output = json.loads(output_json)

        self.assertEqual(output, expected_output)

    def test_custom_layout(self):
        """
        JSONFormatter should use a custom dictionary format if specified.
        """
        expected_output = {
            'file': {'funcName': 'main', 'lineno': 116, 'module': 'test'},
            'time': {'asctime': '2012-11-20T23:30:59.111096Z'},
            'logger': {'name': 'main', 'levelname': 'DEBUG'},
            'message': {'message': "in main function ['foo']"}
        }
        custom_layout = {
            'file': ['module', 'funcName', 'lineno'],
            'time': ['asctime'],
            'logger': ['name', 'levelname'],
            'message': ['message']
        }

        formatter = JSONFormatter(layout=custom_layout)
        output_json = formatter.format(FakeLogRecord())
        output = json.loads(output_json)

        self.assertEqual(output, expected_output)

    def test_proccess_extra(self):
        """
        JSONFormatter.process_extra should find all the `extra` parameters on a LogRecord and return them as a dictionary.
        """
        expected_output = {'ip': '127.0.0.1', 'foo': 'asfd'}

        formatter = JSONFormatter()
        output = formatter.process_extra(FakeLogRecord())

        self.assertEqual(output, expected_output)

    def test_custom_json_encoder(self):
        """
        JSONFormatter should use a custom JSON encoder if it is specified.
        """
        expected_output = {'extra': {'ip': '127.0.0.1', 'foo': '101.03'}}
        custom_layout = {'extra': ''}

        formatter = JSONFormatter(
            layout=custom_layout,
            json_encoder=DecimalJSONEncoder
        )

        record = FakeLogRecord()
        record.foo = decimal.Decimal('101.03')

        output_json = formatter.format(record)
        output = json.loads(output_json)

        self.assertEqual(output, expected_output)

    def test_formatDate(self):
        """
        JSONFormatter.formatDate should return a ISO formatted UTC date string.
        """
        expected_output = '2012-11-20T23:30:59.111096Z'
        timestamp = 1353454259.111096

        formatter = JSONFormatter()
        output = formatter.formatDate(timestamp)

        self.assertEqual(output, expected_output)


class FakeLogRecord(object):
    """A fake log record for testing."""
    def __init__(self):
        self.args = ['foo']
        self.levelname = 'DEBUG'
        self.levelno = 10
        self.pathname = 'test.py'
        self.filename = 'test.py'
        self.process = 7821
        self.processName = 'MainProcess'
        self.threadName = 'MainThread'
        self.thread = 140735211397504
        self.funcName = 'main'
        self.lineno = 116
        self.module = 'test'
        self.relativeCreated = 8.126974105834961
        self.created = 1353454259.111096
        self.name = 'main'
        self.msg = 'in main function %s'
        self.ip = '127.0.0.1'
        self.foo = 'asfd'

    def getMessage(self):
        return self.msg % self.args


class DecimalJSONEncoder(json.JSONEncoder):
    """A JSON encoder that understands decimal objects."""
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DecimalJSONEncoder, self).default(o)
