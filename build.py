"""Static build: runs the GraphQL query in Python and writes index.html (repo root,
for GitHub Pages) and dist/index.html with the result baked in.

    python build.py
"""
import base64
import json
import re
import sys
from pathlib import Path

from server.schema import schema, PAGE_QUERY

ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
DIST = ROOT / "dist"


def main() -> None:
    result = schema.execute_sync(PAGE_QUERY)
    if result.errors:
        sys.exit(f"GraphQL errors: {result.errors}")

    html = (STATIC / "index.html").read_text()
    css = (STATIC / "styles.css").read_text()
    js = (STATIC / "app.js").read_text()

    # Keep the query in app.js and server/schema.py identical.
    m = re.search(r"const PAGE_QUERY = `(.*?)`;", js, re.S)
    if not m or m.group(1).strip() != PAGE_QUERY.strip():
        sys.exit("PAGE_QUERY in static/app.js does not match server/schema.py")

    # Inline the photos so dist/index.html is one self-contained file.
    photo = result.data["profile"]["photo"]
    for key in ("src", "thumb"):
        img = ROOT / photo[key].lstrip("/")
        photo[key] = "data:image/jpeg;base64," + base64.b64encode(img.read_bytes()).decode()

    data = json.dumps(result.data, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace('<link rel="stylesheet" href="/static/styles.css">', f"<style>\n{css}</style>")
    html = html.replace(
        '<script src="/static/app.js"></script>',
        f"<script>window.__PORTFOLIO__ = {data};</script>\n<script>\n{js}</script>",
    )
    DIST.mkdir(exist_ok=True)
    (DIST / "index.html").write_text(html)
    # GitHub Pages serves index.html from the repo root, so write a copy there too.
    (ROOT / "index.html").write_text(html)
    print(f"Wrote index.html and dist/index.html ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
