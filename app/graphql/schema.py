import strawberry
from strawberry.schema import Schema

from app.graphql.mutations.editor import EditorMutation
from app.graphql.queries.address import AddressQuery
from app.graphql.queries.customer import CustomerQuery
from app.graphql.queries.site import SiteQuery


@strawberry.type
class Query(AddressQuery, SiteQuery, CustomerQuery):
    pass


@strawberry.type
class Mutation(EditorMutation):
    pass


schema = Schema(query=Query, mutation=Mutation)
