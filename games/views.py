from django.shortcuts import render
from .models import Shooter, ShooterGame, RPG, RPGGame, Sports

# Create your views here.
def index(request):
    return HttpResponse('hello world')