# Lydia Cortez Portfolio

Python + GraphQL backend (FastAPI + Strawberry), plain HTML/CSS/JS frontend.

```
server/content.py   all site copy: edit this to change the text
server/schema.py    GraphQL types and the page query
server/app.py       FastAPI app: serves the site and /graphql
static/             index.html, styles.css, app.js
build.py            makes a single static file in dist/ for free hosting
```

## Run it live
```
pip install -r requirements.txt
uvicorn server.app:app --reload
```
Open http://127.0.0.1:8000. The GraphQL explorer is at http://127.0.0.1:8000/graphql.

## Publish for free (GitHub Pages, Netlify)
```
python build.py
```
Upload `dist/index.html`. It runs the same GraphQL query at build time and bakes in the result,
so it needs no server. Re-run the build after editing `server/content.py`.

To host the live GraphQL version instead, deploy the FastAPI app to Render, Railway, or Fly.io
with the start command `uvicorn server.app:app --host 0.0.0.0 --port $PORT`.
