import json
from rest_framework import status
from django.urls import reverse
from ..models import Goal
from ..serializers import GoalSerializer

client = Client()
