import config
import generative_AI
import template

from . import prompts


def review():
    return {}


def generate(gai, todo_list):
    parameters = {
        "goals": config.goals,
        "theme": gai.theme.content,
        "tasks": todo_list,
        "review_metadata": gai.reviews.content.get("metadata"),
    }
    user_prompts_text = template.generate(prompts.user, params=parameters)
    prompt = [
        generative_AI.system_prompt(prompts.system),
        generative_AI.user_prompt(user_prompts_text),
    ]
    gai.submit_prompt("gratitude", prompt)
    return gai.gratitude.content
