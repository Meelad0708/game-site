from rest_framework import serializers
from .models import Shooter, ShooterGame, SportsGame, Sports, RPGGame, RPG


class ShooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shooter
        fields = '__all__'


class ShooterGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShooterGame
        fields = ('title', 'genre', 'rating', 'release', 'publisher')


class RPGSerializer(serializers.ModelSerializer):
    class Meta:
        model = RPG
        fields = '__all__'


class RPGGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RPGGame
        fields = ('title', 'genre', 'rating', 'release', 'publisher')


class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'


class SportsGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsGame
        fields = ('title', 'genre', 'rating', 'release', 'publisher')
