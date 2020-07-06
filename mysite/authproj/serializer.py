from rest_framework import serializer
from .models import Goal

class GoalSerializer(serializers.Modelserializer):
    class Meta:
        model = Goal
        fields = ('current', 'previous', 'goal', 'user')