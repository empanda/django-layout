from django.utils import unittest
from django.test.utils import override_settings
import mock

import uuid
from django.http import HttpResponse, HttpRequest

from .request_id import RequestIdMiddleware


class RequestIdMiddlewareTests(unittest.TestCase):
    def get_process_response(self, request_id='requestid', request=None, response=None, rim=None):
        """
        Builds up the required objects to pass to
        RequestIdMiddleware.process_response().

        Passing in an object for request_id, request, response, or
        RequestIdMiddleware overwrites the default.

        Returns a 3 item tuple with, the result of process_response(), the
        header value used, and the request id used.
        """
        request = request
        if not request:
            request = HttpRequest()
            request.id = request_id

        response = response
        if not response:
            response = HttpResponse()

        rim = rim
        if not rim:
            rim = RequestIdMiddleware()

        return (rim.process_response(request, response),
                rim.REQUEST_ID_HEADER,
                request_id)

    def test_process_request_adds_id(self):
        """RequestIdMiddleware should add a UUID to the requests as the `id` attribute."""
        rim = RequestIdMiddleware()
        request = mock.MagicMock()

        rim.process_request(request)

        self.assertIsInstance(request.id, uuid.UUID)

    def test_process_response_adds_header(self):
        """RequestIdMiddleware should add a header to the response with the request id as the value."""
        response, header, request_id = self.get_process_response()

        self.assertIn(header, response)
        self.assertEqual(response[header], request_id)

    @override_settings(REQUEST_ID_HEADER=None)
    def test_process_response_does_not_add_header_when_turned_off(self):
        """RequestIdMiddleware should not add a header to the response when the header is turned off."""
        response, _, _ = self.get_process_response()
        header = 'X-REQUEST-ID'

        self.assertNotIn(header, response)

    @override_settings(REQUEST_ID_HEADER='X-CUSTOM-RID-HEADER')
    def test_process_response_adds_custom_header(self):
        """RequestIdMiddleware should add a custom header to the response with the request id as the value."""
        response, header, request_id = self.get_process_response()

        self.assertEqual(header, 'X-CUSTOM-RID-HEADER')
        self.assertIn(header, response)
        self.assertEqual(response[header], request_id)

    def test_process_response_does_not_override_header(self):
        """RequestIdMiddleware should not override an existing header on the response."""
        rim = RequestIdMiddleware()
        response = HttpResponse()
        response[rim.REQUEST_ID_HEADER] = 'existing'
        response, header, request_id = self.get_process_response(response=response)

        self.assertEqual(response[header], 'existing')

    def test_process_response_warns_when_not_adding(self):
        """RequestIdMiddleware should log a warnning when not overriding an existing header on the response."""
        mock_logger = mock.MagicMock()
        rim = RequestIdMiddleware(logger=mock_logger)
        response = HttpResponse()
        response[rim.REQUEST_ID_HEADER] = 'existing'
        response, header, request_id = self.get_process_response(response=response, rim=rim)

        self.assertTrue(mock_logger.warning.called)
