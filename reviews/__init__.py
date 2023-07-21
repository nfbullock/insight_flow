from random import shuffle

from . import questions
import utilities

FILES = {
    "today": f"data/{utilities.TODAY}-review.json",
    "yesterday": f"data/{utilities.YESTERDAY}-review.json"
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
    

def generate(data, review_type):
    pass


def write(data, review_type):
    file_name = FILES.get(review_type)
    utilities.write_data(file_name, data)