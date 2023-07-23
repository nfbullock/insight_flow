from random import shuffle

from . import prompts, questions
import generative_AI
import config
import template
import utilities

FILES = {
    "today": f"data/{utilities.TODAY}-review.json",
    "yesterday": f"data/{utilities.YESTERDAY}-review.json",
}


def record_daily():
    prompts = getattr(questions, "daily")
    shuffle(prompts)
    responses = {}
    for prompt in prompts:
        response = input(f"{prompt}\n")
        if response:
            responses[prompt] = response
    return responses


def fetch(review_type):
    file_name = FILES.get(review_type)
    return utilities.read_data(file_name, json_load=True)


def generate_yesterday(gai, previous_metadata):
    print(gai.__dict__)
    gai.create_model("reviews", sub_prompts=True)
    print(gai.__dict__)
    user_prompts_text = {
        "tasks": template.generate(prompts.tasks, params=previous_metadata),
        "micro_journals": template.generate(
            prompts.micro_journals, params=previous_metadata
        ),
        "reflection": template.generate(
            prompts.reflection, params=previous_metadata
        ),
    }
    system_prompt = generative_AI.system_prompt(
        template.generate(
            prompts.system,
            params={
                "interests": config.interests,
                "goals": config.goals,
                "theme": gai.theme,
            },
        )
    )
    for name, text in user_prompts_text.items():
        _prompt = [system_prompt, generative_AI.user_prompt(text)]
        gai.submit_prompt("reviews", _prompt, sub_prompt_key=name)


def write(data, review_type):
    file_name = FILES.get(review_type)
    utilities.write_data(file_name, data)
