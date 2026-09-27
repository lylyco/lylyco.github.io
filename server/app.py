"""Run locally:  uvicorn server.app:app --reload   then open http://127.0.0.1:8000
GraphiQL explorer: http://127.0.0.1:8000/graphql"""
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from strawberry.fastapi import GraphQLRouter
from .schema import schema

STATIC = Path(__file__).resolve().parent.parent / "static"

app = FastAPI(title="Lydia Cortez Portfolio")
app.include_router(GraphQLRouter(schema), prefix="/graphql")
app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")
