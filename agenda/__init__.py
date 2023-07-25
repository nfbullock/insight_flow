import config
import generative_AI
import template

from . import prompts


def review():
    return {}


def generate(gai, todo_list):
    parameters = {
        "alignments": config.interests + config.principles + config.goals,
        "theme": gai.theme.content,
        "tasks": todo_list,
        "review_metadata": gai.reviews.content.get("metadata"),
    }
    gai.create_model("agenda", sub_prompts=True)
    user_prompts_text = {
        "alignment": template.generate(prompts.alignment, params=parameters),
        "motivation": template.generate(prompts.motivation, params=parameters),
    }
    system_prompt = generative_AI.system_prompt(prompts.system)
    for name, text in user_prompts_text.items():
        _prompt = [system_prompt, generative_AI.user_prompt(text)]
        gai.submit_prompt("agenda", _prompt, sub_prompt_key=name)
    return gai.agenda.content
