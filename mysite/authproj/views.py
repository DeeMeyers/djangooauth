from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Goal, User
from .serializers import GoalSerializer


def index(request):
    return render(request, 'base.html')

def userpage(request):
    goal = Goal.objects.get(user=request.user)
    diff = goal.current - goal.previous
    remainder = goal.goal - goal.current
    lastLogin = User.objects.get(username=request.user).last_login
    
    return render(request, 'core/page1.html', {'goal': goal, 'diff': diff, 'lastLogin': lastLogin, 'remainder': remainder})

def userpage2(request):
    goal = Goal.objects.get(user=request.user)
    diff = goal.current - goal.previous
    remainder = goal.goal - goal.current
    lastLogin = User.objects.get(username=request.user).last_login
    percent = round((goal.current/goal.goal)*100)
    
    return render(request, 'core/page2.html', {'goal': goal, 'diff': diff, 'lastLogin': lastLogin, 'remainder': remainder, 'percent': percent})

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_goal(request, pk):
    try:
        goal = Goal.objects.get(pk=pk)
    except Goal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GoalSerializer(goal)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        serializer = GoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_goal(request):
    if request.method == 'GET':
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response({})     