from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Goal, User
from .serializer import status


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
        goal = Goal.object.get(pk=pk)
    except Goal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_goal(request):
    elif request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        return Response({})