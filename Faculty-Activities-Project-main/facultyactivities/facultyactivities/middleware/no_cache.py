from django.utils.deprecation import MiddlewareMixin
from django.utils.cache import add_never_cache_headers


class NoCacheForAuthPages(MiddlewareMixin):
    def process_response(self, request, response):
        # Prevent caching of pages for authenticated sessions so back button doesn't show stale content
        if request.user.is_authenticated:
            add_never_cache_headers(response)
        return response

