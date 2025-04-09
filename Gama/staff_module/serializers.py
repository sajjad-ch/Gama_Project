from rest_framework import serializers

from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
        read_only_fields = ['id']


class CollabrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collabrations
        fields = "__all__"
        read_only_fields = ["id"]


class HumanRecourceNeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanRecourceNeed
        fields = "__all__"
        read_only_fields = ["id"]
        