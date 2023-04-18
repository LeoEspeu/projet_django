import os
from pprint import  pprint

from django.core.exceptions import MiddlewareNotUsed
from django.db import connection

class WatcherMiddleware:
    def __init__(self, get_response):
        if not os.getenv('DJANGO_DEBUG_VERBOSE'):
            raise MiddlewareNotUsed
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        pprint(connection.queries)

        return response