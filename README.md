# Lydia Cortez Portfolio

Python + GraphQL backend (FastAPI + Strawberry), plain HTML/CSS/JS frontend.

```
server/content.py   all site copy: edit this to change the text
server/schema.py    GraphQL types and the page query
server/app.py       FastAPI app: serves the site, project pages, and /graphql
server/pages.py     renders each project page (case study or coming soon)
static/             index.html, styles.css, app.js, project.html, page.js, img/
samples/            SQL shown on project pages
build.py            writes index.html and projects/<name>/index.html for GitHub Pages
```

## One-time setup (use a virtual environment)
Installing into Anaconda's base environment can break Jupyter, so keep this project separate:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Run `source .venv/bin/activate` again each time you open a new terminal for this project.

## Preview locally with the live GraphQL server
```
uvicorn server.app:app --reload
```
Open http://127.0.0.1:8000. The GraphQL explorer is at http://127.0.0.1:8000/graphql.
Press Ctrl+C to stop the server before typing other commands in that terminal.

## Publish to GitHub Pages
```
python build.py
git add .
git commit -m "Update site"
git push
```
`build.py` runs the same GraphQL query and saves the result into `index.html` at the repo root,
which is the file GitHub Pages serves. Re-run it every time you edit `server/content.py`,
the styles, or the photos.
