import utilities
import reviews
import daily_motif
import faster
import gratitude
import agenda
import eater
import marriage
import kidtext
import sponsord
import coder
import generative_AI
import secrets
import todo


if __name__ == "__main__":
    gai = generative_AI.Chat(secrets.OPEN_AI_TOKEN)
    previous_day = reviews.fetch("yesterday")
    daily_motif.generate(gai, previous_day)
    fasted_metadata = faster.generate(previous_day)
    content = {
        "theme": gai.theme.content,
        "gratitude": gratitude.generate(gai),
        "previous_day": reviews.generate_yesterday(gai, previous_day),
        # "agenda": agenda.generate(gai, previous_day),
        "todo": todo.generate(),
        "faster": fasted_metadata,
        "eater": eater.generate(gai, fasted_metadata),
        "marriage": marriage.generate(gai),
        "kidtext": kidtext.generate(gai),
        "sponsord": sponsord.generate(gai),
        "coder": coder.generate(gai),
        "wisdom": wisdom.generate(gai, previous_day),
    }
    utilities.write_data(content_file, content)
