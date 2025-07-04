from django.shortcuts import render

from .models import *
from .serializers import *
from .utils import CsrfExemptViewSetMixin

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class CollabrationsViewSet(CsrfExemptViewSetMixin, viewsets.ModelViewSet):
    queryset = Collabrations.objects.all()
    serializer_class = CollabrationsSerializer
    # permission_classes = [permissions.AllowAny]


class HumanRecourceNeedViewSet(CsrfExemptViewSetMixin, viewsets.ModelViewSet):
    queryset = HumanRecourceNeed.objects.all()
    serializer_class = HumanRecourceNeedSerializer
    # permission_classes = [permissions.AllowAny]
    