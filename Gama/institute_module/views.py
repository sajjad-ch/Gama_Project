from django.shortcuts import render

from .models import *
from .serializers import *

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAdminUser]


class RegisteraionViewSet(viewsets.ModelViewSet):
    queryset = Registeration.objects.all()
    serializer_class = RegisterationSerializer
    permission_classes = [permissions.AllowAny]


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    # permission_classes = [permissions.IsAdminUser]


class CommentAndSuggestionViewSet(viewsets.ModelViewSet):
    queryset = CommentsAndSuggestions.objects.all()
    serializer_class = CommentsAndSuggestionsSerializer
    permission_classes = [permissions.AllowAny]
