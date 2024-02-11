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


class ShooterGameMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        genre = graphene.ID(required=True)
        rating = graphene.Int()
        release = graphene.DateTime()
        publisher = graphene.String()

    shooter_game = graphene.Field(ShooterGameType)

    @classmethod
    def mutate(cls, root, info, title, genre, rating, release, publisher):
        shooter = Shooter.objects.get(id=genre)

        shooter_game = ShooterGame()
        shooter_game.title = title
        shooter_game.genre = shooter
        shooter_game.rating = rating
        shooter_game.release = release
        shooter_game.publisher = publisher

        shooter_game.save()

        return ShooterGameMutation(shooter_game=shooter_game)


class RPGGameMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        genre = graphene.ID(required=True)
        rating = graphene.Int()
        release = graphene.DateTime()
        publisher = graphene.String()

    rpg_game = graphene.Field(RPGGameType)

    @classmethod
    def mutate(cls, root, info, title, genre, rating, release, publisher):
        rpg = RPG.objects.get(id=genre)

        rpg_game = RPGGame()
        rpg_game.title = title
        rpg_game.genre = rpg
        rpg_game.rating = rating
        rpg_game.release = release
        rpg_game.publisher = publisher

        rpg_game.save()

        return RPGGameMutation(rpg_game=rpg_game)


class SportsGameMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        genre = graphene.ID(required=True)
        rating = graphene.Int()
        release = graphene.DateTime()
        publisher = graphene.String()

    sports_game = graphene.Field(SportsGameType)

    @classmethod
    def mutate(cls, root, info, title, genre, rating, release, publisher):
        sport = Sports.objects.get(id=genre)

        sports_game = SportsGame()
        sports_game.title = title
        sports_game.genre = sport
        sports_game.rating = rating
        sports_game.release = release
        sports_game.publisher = publisher

        sports_game.save()

        return SportsGameMutation(sports_game=sports_game)


class Mutation(graphene.ObjectType):
    create_shooter_game = ShooterGameMutation.Field()
    create_rpg_game = RPGGameMutation.Field()
    create_sports_game = SportsGameMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
