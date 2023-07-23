import generative_AI, template

from . import prompts


def generate(gai, parameters):
    user_prompt_text = template.generate(prompt.user, params=parameters)
    messages = [
        generative_AI.system_prompt(prompts.system),
        generative_AI.user_prompt(user_prompt_text),
    ]
    gai.submit_prompt("eater", messages)
