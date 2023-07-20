import datetime
import json
import os

import pytz

import agenda
import coder
import config
import daily_motif
import eater
import faster
import gratitude
import kidtext
import marriage
import notes
import reviews
import sponsord
import todo
import utilities


def _collision(_file):
    prompt = "File exists, overwrite? (Y/n)"
    return os.path.isfile(_file) and bool(input(prompt) or 0)


if __name__ == "__main__":
    review_file = f"data/{utilities.TODAY}-review.json"
    if _collision(review_file):
        sys.exit(0)
    utilities.nag_prompt("Tidy your spaces")
    review = {
        "agenda": agenda.review(),
        "coder": coder.review(),
        "daily_motif": daily_motif.review(),
        "eater": eater.review(),
        "faster": faster.review(),
        "gratitude": gratitude.review(),
        "kidtext": kidtext.review(),
        "marriage": marriage.review(),
        "sponsord": sponsord.review(),
        "todo": todo.review(),
        "notes": notes.review(),
        "prompts": reviews.record_daily(),
    }
    utilities.write_data(review_file, review)
