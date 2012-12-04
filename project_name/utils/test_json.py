from django.utils import unittest
import decimal
import uuid
import datetime
import Cookie

from django.test.client import RequestFactory
from django.http import HttpResponse

from .json import ExtendedJSONEncoder


class ExtendedJSONEncoderTests(unittest.TestCase):
    def assertExtendedJSONEncoderReturns(self, input, expected):
        """A shorthand assertion for ExtendedJSONEncoder.default() equality."""
        output = ExtendedJSONEncoder().default(input)
        self.assertEqual(output, expected)

    def test_supports_datetime_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a datetime.datetime."""
        dt = datetime.datetime(2012, 11, 26, 17, 28, 40, 56808)
        self.assertExtendedJSONEncoderReturns(dt, '2012-11-26T17:28:40.056')

    def test_supports_date_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a datetime.date."""
        d = datetime.date(2012, 11, 26)
        self.assertExtendedJSONEncoderReturns(d, '2012-11-26')

    def test_supports_time_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a datetime.time."""
        t = datetime.time(17, 28, 40, 56808)
        self.assertExtendedJSONEncoderReturns(t, '17:28:40.056')

    def test_supports_decimal_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a decimal.Decimal."""
        d = decimal.Decimal('1.51')
        self.assertExtendedJSONEncoderReturns(d, '1.51')

    def test_supports_uuid_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a uuid.UUID."""
        id = uuid.uuid4()
        self.assertExtendedJSONEncoderReturns(id, str(id))

    def test_supports_simplecookie_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a Cookie.SimpleCookie."""
        c = Cookie.SimpleCookie()
        self.assertExtendedJSONEncoderReturns(c, {})

    def test_supports_httprequest_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a django.http.HttpRequest."""
        r = RequestFactory().get('/')
        self.assertExtendedJSONEncoderReturns(r, {'method': 'GET',
            'session': None, 'META': {'HTTP_COOKIE': ''}, 'user': None,
            'id': None, 'path_info': u'/'})

    def test_supports_httpresponse_objects(self):
        """ExtendedJSONEncoder should return a JSON representation of a django.http.HttpResponse."""
        r = HttpResponse()
        self.assertExtendedJSONEncoderReturns(r,
            {'status_code': 200, 'cookies': Cookie.SimpleCookie(),
             'headers': {'content-type': ('Content-Type', 'text/html; charset=utf-8')}})
