"""Run locally:  uvicorn server.app:app --reload   then open http://127.0.0.1:8000
GraphiQL explorer: http://127.0.0.1:8000/graphql"""
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from strawberry.fastapi import GraphQLRouter
from .schema import schema
from .pages import projects_with_pages, project_slug, render_project_page

STATIC = Path(__file__).resolve().parent.parent / "static"

app = FastAPI(title="Lydia Cortez Portfolio")
app.include_router(GraphQLRouter(schema), prefix="/graphql")
app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


@app.get("/projects/{slug}/", response_class=HTMLResponse)
def project_page(slug: str):
    for p in projects_with_pages():
        if project_slug(p["url"]) == slug:
            return render_project_page(
                p,
                styles='<link rel="stylesheet" href="/static/styles.css">',
                script='<script src="/static/page.js"></script>',
            )
    raise HTTPException(status_code=404)
