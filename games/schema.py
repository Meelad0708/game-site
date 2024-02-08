import graphene
from graphene_django import DjangoObjectType
from .models import Shooter, ShooterGame, RPGGame, RPG, SportsGame, Sports


class ShooterType(DjangoObjectType):
    class Meta:
        model = Shooter
        fields = ('id', 'name', 'shootergame')


class ShooterGameType(DjangoObjectType):
    class Meta:
        model = ShooterGame
        fields = ('id', 'title', 'genre', 'rating', 'release', 'publisher', 'description')


class RPGType(DjangoObjectType):
    class Meta:
        model = RPG
        fields = ('id', 'name', 'rpggame')


class RPGGameType(DjangoObjectType):
    class Meta:
        model = RPGGame
        fields = ('id', 'title', 'genre', 'rating', 'release', 'publisher', 'description')


class SportsType(DjangoObjectType):
    class Meta:
        model = Sports
        fields = ('id', 'name', 'sportsgame')


class SportsGameType(DjangoObjectType):
    class Meta:
        model = SportsGame
        fields = ('id', 'title', 'genre', 'rating', 'release', 'publisher', 'description')


class Query(graphene.ObjectType):
    all_shootergame = graphene.List(ShooterGameType)
    shooter_by_name = graphene.Field(ShooterType, name=graphene.String(required=True))
    all_rpggame = graphene.List(RPGGameType)
    rpg_by_name = graphene.Field(RPGType, name=graphene.String(required=True))
    all_sportsgame = graphene.List(SportsGameType)
    sports_by_name = graphene.Field(SportsType, name=graphene.String(required=True))

    def resolve_all_shootergame(root, info):
        return ShooterGame.objects.select_related('genre').all()

    def resolve_shooter_by_name(root, info, name):
        try:
            return Shooter.objects.get(name=name)
        except Shooter.DoesNotExist:
            return None

    def resolve_all_rpggame(root, info):
        return RPGGame.objects.select_related('genre').all()

    def resolve_rpg_by_name(root, info, name):
        try:
            return RPG.objects.get(name=name)
        except RPG.DoesNotExist:
            return None

    def resolve_all_sportsgame(root, info):
        return SportsGame.objects.select_related('genre').all()

    def resolve_sports_by_name(root, info, name):
        try:
            return Sports.objects.get(name=name)
        except Sports.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
