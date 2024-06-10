from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework import serializers
from api.quickstart.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'api.quickstart'
        model = Task
        fields = ['id', 'name', 'start_date', 'durations', 'place']
        read_only_fields = ['creator']

