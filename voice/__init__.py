import generative_AI
import template
import utilities

from . import prompts

FILES = {"previous": "data/voice.json"}


def review():
    return {}


def generate(gai):
    parameters = {"theme": gai.theme.content, "voice": {}}
    user_prompt_text = template.generate(prompts.user, params=parameters)
    messages = [
        generative_AI.system_prompt(prompts.system),
        generative_AI.user_prompt(user_prompt_text),
    ]
    gai.submit_prompt("voice", messages)
    return gai.voice.content
