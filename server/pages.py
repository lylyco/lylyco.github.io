"""Renders the "coming soon" page for each project from static/project.html."""
from html import escape
from pathlib import Path

from . import content as c

STATIC = Path(__file__).resolve().parent.parent / "static"


def project_slug(url: str) -> str:
    """"/projects/project-1/" -> "project-1"."""
    return url.strip("/").split("/")[-1]


def render_project_page(project: dict, *, styles: str, script: str) -> str:
    footer = c.FOOTER
    values = {
        "title": project["title"],
        "name": c.PROFILE["name"],
        "footer_credit": footer["credit"],
        "footer_source_url": footer["source_url"],
        "footer_source_label": footer["source_label"],
        "footer_legal": footer["legal"],
    }
    html = (STATIC / "project.html").read_text()
    for key, value in values.items():
        html = html.replace("{{" + key + "}}", escape(value))
    return html.replace("{{styles}}", styles).replace("{{script}}", script)


def projects_with_pages() -> list:
    return [p for p in c.PROJECTS["items"] if p["url"]]
