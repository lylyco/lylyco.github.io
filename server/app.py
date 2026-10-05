"""Run locally:  uvicorn server.app:app --reload   then open http://127.0.0.1:8000
GraphiQL explorer: http://127.0.0.1:8000/graphql"""
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from strawberry.fastapi import GraphQLRouter
from .schema import schema
from .pages import projects_with_pages, project_slug, render_project_page

STATIC = Path(__file__).resolve().parent.parent / "static"

app = FastAPI(title="Lydia Cortez Portfolio")
app.include_router(GraphQLRouter(schema), prefix="/graphql")
app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.middleware("http")
async def no_stale_files(request, call_next):
    # Make the browser re-check styles and scripts on every load, so edits show up
    # right away when previewing locally instead of an old cached copy.
    response = await call_next(request)
    if request.url.path.startswith("/static/"):
        response.headers["Cache-Control"] = "no-cache"
    return response


def _versioned(name: str) -> str:
    """'/static/styles.css?v=<last edit time>': a new address after every edit, so the
    browser can never reuse an old cached copy while previewing locally."""
    return f"/static/{name}?v={int((STATIC / name).stat().st_mtime)}"


@app.get("/", response_class=HTMLResponse)
def index():
    html = (STATIC / "index.html").read_text()
    for name in ("styles.css", "app.js"):
        html = html.replace(f'"/static/{name}"', f'"{_versioned(name)}"')
    return html


@app.get("/projects/{slug}/", response_class=HTMLResponse)
def project_page(slug: str):
    for p in projects_with_pages():
        if project_slug(p["url"]) == slug:
            return render_project_page(
                p,
                styles=f'<link rel="stylesheet" href="{_versioned("styles.css")}">',
                script=f'<script src="{_versioned("page.js")}"></script>',
            )
    raise HTTPException(status_code=404)
