from django.shortcuts import render
from django.http import HttpResponse
from .models import Goal, User


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
