from rest_framework import serializers
from .models import Task
import ipdb

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'tag', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['is_active', 'created_at', 'updated_at']


class TaskCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'tag', 'is_active', 'created_at', 'updated_at']
        read_only_field  = ['id', 'title', 'tag', 'created_at', 'updated_at']