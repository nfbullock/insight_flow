import pprint
from random import shuffle

import config
import generative_AI
import template
import utilities

from . import prompts, questions

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
    gai.create_model("reviews", sub_prompts=True)
    previous_metadata["theme"] = gai.theme.content
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
                "theme": gai.theme.content,
            },
        )
    )
    for name, text in user_prompts_text.items():
        _prompt = [system_prompt, generative_AI.user_prompt(text)]
        gai.submit_prompt("reviews", _prompt, sub_prompt_key=name)
    metadata_prompt_text = template.generate(
        prompts.metadata, params={"reviews": gai.reviews.content}
    )
    metadata_prompt = [generative_AI.user_prompt(metadata_prompt_text)]
    gai.submit_prompt(
        "reviews",
        metadata_prompt,
        sub_prompt_key="metadata",
        load_response=True,
    )
    return gai.reviews.content


def write(data, review_type):
    file_name = FILES.get(review_type)
    utilities.write_data(file_name, data)
