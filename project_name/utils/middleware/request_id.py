import uuid
import logging

from django.conf import settings


class RequestIdMiddleware(object):
    """
    Add a unique ID to each request. The ID is generated using a uuid.

    This middleware is useful when trying to trace a request through the logs.

    If you are using the JSONFormatter for logging and you include a request
    object in your `extra` dictionary passed to logging calls, this ID will be
    displayed in the final JSON output.
    """
    def __init__(self, REQUEST_ID_HEADER='X-REQUEST-ID', logger=None):
        self.REQUEST_ID_HEADER = getattr(settings, 'REQUEST_ID_HEADER', REQUEST_ID_HEADER)

        self.logger = logger
        if not logger:
            self.logger = logging.getLogger(__name__)

    def process_request(self, request):
        """Add request.id as a new random UUID."""
        request.id = uuid.uuid4()

    def process_response(self, request, response):
        """
        Add a header with the request.id as the value to the response.

        The header name is controlled via the REQUEST_ID_HEADER setting. If
        REQUEST_ID_HEADER is None then the header is not added.

        Example header:
            X-REQUEST-ID: 1c7b5522-ccec-4506-bda4-1f218a344b85
        """
        request_id = getattr(request, 'id', None)
        if self.REQUEST_ID_HEADER and request_id:
            if self.REQUEST_ID_HEADER not in response:
                response[self.REQUEST_ID_HEADER] = request_id
            else:
                self.logger.warning(
                    '%s header already in response, request id not added',
                    self.REQUEST_ID_HEADER,
                    extra={'request': request, 'response': response}
                )

        return response
