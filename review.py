import datetime
import pytz
import json
import os
import config

import reviews
import notes
import todo

def _collision(_file):
    prompt = "File exists, overwrite? (Y/n)"
    return os.path.isfile(_file) and bool(input(prompt) or 0)

def _create_file():
    now = datetime.datetime.now(pytz.timezone(config.timezone))
    return now.date().strftime(f"data/{config.date_str}.json")

if __name__ == "__main__":
    review_file = _create_file()
    if _collision(review_file):
        sys.exit(0)
    review = {
        "todo": todo.review(),
        "notes": notes.review(),
        "prompts": reviews.review("daily")
    }
    with open(review_file, "w") as f:
        json.dump(review, f,sort_keys=True, indent=True)
