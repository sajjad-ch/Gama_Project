# utils.py
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class CsrfExemptViewSetMixin:
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        return csrf_exempt(view)
