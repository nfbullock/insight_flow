from random import shuffle

from . import questions

def review(question_type):
    prompts = getattr(questions, question_type)
    shuffle(prompts)
    responses = {}
    for prompt in prompts:
        response = input(f"{prompt}\n")
        if response:
            responses[prompt] = response
    return responses

