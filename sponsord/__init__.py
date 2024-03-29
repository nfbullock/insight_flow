import generative_AI
import template

from . import prompts


def review():
    return {}


def generate(gai):
    parameters = {"theme": gai.theme.content}
    user_prompt_text = template.generate(prompts.user, params=parameters)
    messages = [
        generative_AI.system_prompt(prompts.system),
        generative_AI.user_prompt(user_prompt_text),
    ]
    gai.submit_prompt("sponsord", messages)
    return gai.sponsord.content
