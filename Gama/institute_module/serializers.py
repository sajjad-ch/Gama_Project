from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ['id']


class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registeration
        fields = "__all__"
        read_only_fields = ['id']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__"
        read_only_fields = ['id']
