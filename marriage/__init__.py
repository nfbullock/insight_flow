import config
import generative_AI
import template

from . import prompts


def review():
    return {}


def generate(gai):
    parameters = {
        "challenging_areas": config.marriage_struggles,
        "theme": gai.theme.content,
    }
    user_prompts_text = template.generate(prompts.user, params=parameters)
    prompt = [
        generative_AI.system_prompt(prompts.system),
        generative_AI.user_prompt(user_prompts_text),
    ]
    gai.submit_prompt("marriage", prompt)
    return gai.marriage.content
