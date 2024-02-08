import graphene
from games.schema import Query as games_query
from games.schema import Mutation as games_mutation


class Mutation(games_mutation):
    pass


class Query(games_query):
    pass

schema= graphene.Schema(query=Query, mutation=Mutation)