import strawberry
from strawberry.schema import Schema

from app.graphql.queries.address import AddressQuery
from app.graphql.queries.site import SiteQuery


@strawberry.type
class Query(AddressQuery, SiteQuery):
    pass


schema = Schema(query=Query)
