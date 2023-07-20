from random import shuffle

from . import questions
import utilities


def record_daily():
    prompts = getattr(questions, "daily")
    shuffle(prompts)
    responses = {}
    for prompt in prompts:
        response = input(f"{prompt}\n")
        if response:
            responses[prompt] = response
    return responses


def generate(review_type, metadata):
    pass
