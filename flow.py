import secrets

import agenda
import coder
import eater
import faster
import generative_AI
import gratitude
import kidtext
import marriage
import reviews
import sponsord
import theme
import todo
import utilities
import voice

if __name__ == "__main__":
    gai = generative_AI.Chat(secrets.OPEN_AI_TOKEN)
    previous_day = reviews.fetch("yesterday")
    fasted_metadata = faster.generate(previous_day)
    todo_list = todo.generate()
    content = {
        "theme": theme.generate(gai, previous_day),
        "reviews": reviews.generate_yesterday(gai, previous_day),
        "agenda": agenda.generate(gai, todo_list),
        "gratitude": gratitude.generate(gai, todo_list),
        "todo": todo_list,
        "faster": fasted_metadata,
        "eater": eater.generate(gai, fasted_metadata),
        "marriage": marriage.generate(gai),
        "kidtext": kidtext.generate(gai),
        "sponsord": sponsord.generate(gai),
        "voice": voice.generate(gai),
    }
    utilities.write_data(f"data/{utilities.TODAY}-flow.json", content)
