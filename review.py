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


if __name__ == "__main__":
    utilities.nag_prompt("Tidy your spaces")
    review = {
        "agenda": agenda.review(),
        "coder": coder.review(),
        "daily_motif": daily_motif.review(),
        "faster": faster.review(),
        "gratitude": gratitude.review(),
        "kidtext": kidtext.review(),
        "marriage": marriage.review(),
        "sponsord": sponsord.review(),
        "todo": todo.review(),
        "notes": notes.review(),
        "prompts": reviews.record_daily(),
    }
    reviews.write(review, "today")
