import graphene
from games.schema import Query as games_query


class Query(games_query):
    pass

schema= graphene.Schema(query=Query)