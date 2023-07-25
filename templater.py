import json

from markupsafe import escape

import template
import utilities

FILE = "data/20230725-flow.json"


def str_to_html_secure(input_str):
    # Escape any HTML characters, then replace newline characters with <br/>
    html = input_str.replace("\n", "<br/>")
    return html


def cast_strings_in_dict(content_):
    for k, v in content_.items():
        if isinstance(v, str):
            content_[k] = str_to_html_secure(v)
    return content_


with open(FILE) as f:
    content = json.load(f)

sorted_todo = sorted(
    content.pop("todo"), key=lambda item: item["priority"], reverse=True
)


params = {
    "theme": cast_strings_in_dict(content.pop("theme")),
    "todo": sorted_todo,
    "agenda": cast_strings_in_dict(content.pop("agenda")),
    "reviews": cast_strings_in_dict(content.pop("reviews")),
    "kidtext": cast_strings_in_dict(content.pop("kidtext")),
    "content": cast_strings_in_dict(content),
}

html = template.generate_from_file("template/html.j2", params)
with open("flow.html", "w") as f:
    f.write(html)
