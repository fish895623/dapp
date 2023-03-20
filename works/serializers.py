from rest_framework import serializers
from .models import Todo
from .models import Works
from .models import WorkTitle
from .models import WorkStatus


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class WorkTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTitle
        fields = "__all__"


class WorkStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkStatus
        fields = "__all__"


class WorksSerializer(serializers.ModelSerializer):
    workTitle = WorkTitleSerializer(source="workid", read_only=True)
    workStatus = WorkStatusSerializer(source="statusid", read_only=True)

    class Meta:
        model = Works
        fields = "__all__"
