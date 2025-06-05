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


class CommentsAndSuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsAndSuggestions
        fields = "__all__"
        read_only_fields = ['id']


class HeadlineCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadlineCourse
        fields = "__all__"
        read_only_fields = ['id']


class LessonsHeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsHeadline
        fields = "__all__"
        read_only_fields = ['id']


class InstitueDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitueData
        fields = "__all__"
        read_only_fields = ['id']
