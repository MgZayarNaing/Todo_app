from rest_framework import serializers
from my_app.models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"
