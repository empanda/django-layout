import uuid

class RequestIdMiddleware(object):
    """
    Add a unique ID to each request. The ID is generated using a uuid.

    This middleware is useful when trying to trace a request through the logs.

    If you are using the JSONFormatter for logging and you include a request
    object in your `extra` dictionary passed to logging calls, this ID will be
    displayed in the final JSON output.
    """
    def process_request(self, request):
        request.id = uuid.uuid4()
