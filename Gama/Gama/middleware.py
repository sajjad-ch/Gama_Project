from django.utils.deprecation import MiddlewareMixin

class DisableCSRFMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/backend/") and request.method in ("POST", "PUT", "PATCH"):
            setattr(request, "_dont_enforce_csrf_checks", True)