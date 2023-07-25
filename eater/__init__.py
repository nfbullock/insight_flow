import random

import generative_AI
import template

from . import cuisine_types, prompts


def get_cuisine():
    return random.choice(cuisine_types.unsorted)


def generate(gai, parameters):
    parameters["cuisine_type"] = get_cuisine()
    user_prompt_text = template.generate(prompts.user, params=parameters)
    messages = [
        generative_AI.system_prompt(prompts.system),
        generative_AI.user_prompt(user_prompt_text),
    ]
    gai.submit_prompt("eater", messages)
    return gai.eater.content
