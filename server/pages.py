"""Renders each project's page from static/project.html: the case study, or "coming soon"."""
import re
from html import escape
from pathlib import Path

from . import content as c

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"


def project_slug(url: str) -> str:
    """"/projects/sana-compliance/" -> "sana-compliance"."""
    return url.strip("/").split("/")[-1]


def _text(s: str) -> str:
    """Escape text, then turn **bold** into <strong>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escape(s))


def _list(items, tag="ul") -> str:
    return f"<{tag}>" + "".join(f"<li>{_text(i)}</li>" for i in items) + f"</{tag}>"


def _case_study(cs: dict) -> str:
    steps = "".join(
        f"<li><strong>{_text(title)}</strong> {_text(body)}</li>" for title, body in cs["steps"]
    )
    parts = [
        f'<h1 class="project-title">{_text(cs["heading"])}<br><em>{_text(cs["heading_emphasis"])}</em></h1>',
        '<div class="case">',
        f'<div class="case-block"><h2>The Problem</h2><p>{_text(cs["problem"])}</p></div>',
        f'<div class="case-block"><h2>What I Did</h2><ol class="case-steps">{steps}</ol></div>',
        f'<div class="case-block"><h2>Impact</h2>{_list(cs["impact"])}</div>',
    ]
    if cs.get("next"):
        parts.append(f'<div class="case-block"><h2>What\'s Next</h2>{_list(cs["next"])}</div>')
    if cs.get("sample"):
        parts.append(_sample(cs["sample"]))
    parts.append("</div>")
    return "\n    ".join(parts)


SQL_KEYWORDS = {
    "SELECT", "FROM", "WHERE", "AND", "OR", "NOT", "AS", "ON", "JOIN", "LEFT", "WITH", "CASE",
    "WHEN", "THEN", "ELSE", "END", "IS", "NULL", "NULLS", "LAST", "FIRST", "ORDER", "BY",
    "GROUP", "PARTITION", "OVER", "UNION", "ALL", "DESC", "ASC", "WITHIN", "IN",
}
SQL_FUNCTIONS = {"ROW_NUMBER", "COUNT", "SUM", "LISTAGG", "TO_CHAR", "NVL", "LOWER", "TRIM"}
SQL_TOKEN = re.compile(r"(--[^\n]*)|('(?:[^']|'')*')|\b(\d+)\b|\b([A-Za-z_][A-Za-z0-9_]*)\b")


def _highlight_sql(line: str) -> str:
    """Wrap comments, strings, numbers, keywords and functions in spans for coloring."""
    out, pos = [], 0
    for m in SQL_TOKEN.finditer(line):
        out.append(escape(line[pos:m.start()]))
        comment, string, number, word = m.groups()
        tok = escape(m.group(0))
        if comment:
            out.append(f'<span class="tk-c">{tok}</span>')
        elif string:
            out.append(f'<span class="tk-s">{tok}</span>')
        elif number:
            out.append(f'<span class="tk-n">{tok}</span>')
        elif word.upper() in SQL_KEYWORDS:
            out.append(f'<span class="tk-k">{tok}</span>')
        elif word.upper() in SQL_FUNCTIONS:
            out.append(f'<span class="tk-f">{tok}</span>')
        else:
            out.append(tok)
        pos = m.end()
    out.append(escape(line[pos:]))
    return "".join(out)


def _snippet(path: str) -> str:
    """A code window: file name, line numbers, and a preview that expands."""
    lines = (ROOT / path).read_text().rstrip("\n").split("\n")
    code = "".join(f'<span class="ln">{_highlight_sql(l) or " "}</span>' for l in lines)
    name = escape(Path(path).name)
    return (
        '<div class="snippet">'
        '<div class="snippet-bar"><span class="snippet-dots" aria-hidden="true"><i></i><i></i><i></i></span>'
        f'<span class="snippet-name">{name}</span>'
        '</div>'
        f'<pre class="snippet-code is-collapsed"><code>{code}</code></pre>'
        f'<button class="snippet-toggle" type="button" aria-expanded="false" data-more="Show all {len(lines)} lines" data-less="Show less">Show all {len(lines)} lines</button>'
        "</div>"
    )


def _sample_block(b: dict) -> str:
    if "sql" in b:
        return _snippet(b["sql"])
    if "note" in b:
        return f'<p class="case-note">{_text(b["note"])}</p>'
    if "sheet" in b:
        return (
            f'<iframe class="case-sheet" src="{escape(b["sheet"])}" title="Sample report" loading="lazy"></iframe>'
            f'<p class="case-note"><a href="{escape(b["url"])}" target="_blank" rel="noopener">Open in Google Sheets</a></p>'
        )
    if "image" in b:
        src = escape(b["image"])
        return (
            f'<a class="case-image" href="{src}" target="_blank" rel="noopener" aria-label="Open the full-size image">'
            f'<img src="{src}" alt="{escape(b["alt"])}" loading="lazy"></a>'
        )
    raise ValueError(f"Unknown sample block: {b}")


def _sample(sm: dict) -> str:
    blocks = "".join(_sample_block(b) for b in sm["blocks"])
    return f'<div class="case-block case-sample"><h2>{_text(sm["heading"])}</h2>{blocks}</div>'


def _coming_soon(project: dict) -> str:
    return (
        f'<h1 class="project-title">{_text(project["title"])}<br><em>coming soon.</em></h1>\n'
        '    <p class="project-note">The full write-up for this project is on its way.</p>'
    )


def render_project_page(project: dict, *, styles: str, script: str) -> str:
    footer = c.FOOTER
    cs = project.get("case_study")
    description = project["summary"] if cs else f'{project["title"]}: a project by {c.PROFILE["name"]}. Coming soon.'
    values = {
        "title": project["title"],
        "description": description,
        "url": project["url"],
        "name": c.PROFILE["name"],
        "footer_credit": footer["credit"],
        "footer_source_url": footer["source_url"],
        "footer_source_label": footer["source_label"],
        "footer_legal": footer["legal"],
    }
    html = (STATIC / "project.html").read_text()
    for key, value in values.items():
        html = html.replace("{{" + key + "}}", escape(value))
    body = _case_study(cs) if cs else _coming_soon(project)
    return html.replace("{{body}}", "    " + body).replace("{{styles}}", styles).replace("{{script}}", script)


def projects_with_pages() -> list:
    return [p for p in c.PROJECTS["items"] if p["url"]]
