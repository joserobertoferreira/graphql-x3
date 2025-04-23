from fastapi import FastAPI

from app.routers.routers import graphql_app

app = FastAPI()


app.include_router(graphql_app, prefix='/graphql')
