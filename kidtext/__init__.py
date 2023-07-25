from datetime import datetime

import config
import generative_AI
import template
import utilities

from . import prompts


def review():
    return {}


def _extract_age(child):
    birthday = datetime.strptime(child["birthday"], config.date_str)
    delta = datetime.now() - birthday
    return f"{delta.days} days old"


def generate(gai):
    gai.create_model("kidtext", sub_prompts=True)
    for child in config.kidtext_targets:
        parameters = {
            "theme": gai.theme.content,
            "child_age": _extract_age(child),
        }
        user_text = template.generate(prompts.user, parameters)
        if child.get("additional_task"):
            user_text += f"\n\n{child['additional_task']}"
        messages = [
            generative_AI.system_prompt(prompts.system),
            generative_AI.user_prompt(user_text),
        ]
        gai.submit_prompt("kidtext", messages, sub_prompt_key=child["name"])
    return gai.kidtext.content
