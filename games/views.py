from rest_framework import viewsets
from .models import Shooter, ShooterGame, RPG, RPGGame, Sports, SportsGame
from .game_serializers import ShooterGameSerializer, ShooterSerializer, RPGGameSerializer, RPGSerializer, \
    SportsSerializer, SportsGameSerializer


# Create your views here.
class ShooterViewSet(viewsets.ModelViewSet):
    queryset = Shooter.objects.all()
    serializer_class = ShooterSerializer


class ShooterGameViewSet(viewsets.ModelViewSet):
    queryset = ShooterGame.objects.all()
    serializer_class = ShooterGameSerializer


class RPGViewSet(viewsets.ModelViewSet):
    queryset = RPG.objects.all()
    serializer_class = RPGSerializer


class RPGGameViewSet(viewsets.ModelViewSet):
    queryset = RPGGame.objects.all()
    serializer_class = RPGGameSerializer


class SportsViewSet(viewsets.ModelViewSet):
    queryset = Sports.objects.all()
    serializer_class = SportsSerializer


class SportsGameViewSet(viewsets.ModelViewSet):
    queryset = SportsGame.objects.all()
    serializer_class = SportsGameSerializer
