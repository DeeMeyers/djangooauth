from django.shortcuts import render
from django.http import HttpResponse
from .models import Goal


def index(request):
    return render(request, 'base.html')

def userpage(request):
    goal = Goal.objects.get(user=request.user)
    return render(request, 'core/page1.html', {'goal': goal})