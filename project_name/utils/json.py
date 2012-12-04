from __future__ import absolute_import

import json
import datetime
import uuid
import decimal
import Cookie

from django.http import HttpRequest, HttpResponse
from django.utils.timezone import is_aware


class ExtendedJSONEncoder(json.JSONEncoder):
    """
    A JSON encoder that understands more Python types, including:
      * datetime.datetime
      * datetime.date
      * datetime.time
      * decimal.Decimal
      * uuid.UUID
      * Cookie.SimpleCookie
      * django.http.HttpRequest
      * django.http.HttpResponse

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

        elif isinstance(o, Cookie.SimpleCookie):
            cookies = {}
            for cookie, morsel in o.iteritems():
                cookies[cookie] = dict(morsel)
                cookies[cookie]['value'] = morsel.value
            return cookies

        elif isinstance(o, HttpRequest):
            request = o
            return {
                'session': getattr(getattr(request, 'session', None), '_session_key', None),
                'user': getattr(getattr(request, 'user', None), 'id', None),
                'path_info': request.path_info,
                'method': request.method,
                'id': getattr(request, 'id', None),
                'META': dict([(key, value) for key, value in request.META.iteritems() if key.startswith('HTTP_')]),
            }

        elif isinstance(o, HttpResponse):
            response = o
            return {
                'status_code': response.status_code,
                'headers': response._headers,
                'cookies': response.cookies
            }

        else:
            return super(ExtendedJSONEncoder, self).default(o)
