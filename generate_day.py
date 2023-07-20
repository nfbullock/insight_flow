import utilities

if __name__ == "__main__":
    content_file = f"data/{utilities.TODAY}-daily_flow.json"
    previous_day = review.fetch_yesterday()
    theme = daily_motif(previous_day)
    fasted_metadata = faster.generate(theme, previous_day)
    content = {
        "theme": theme,
        "gratitude": gratitude.generate(theme),
        "previous_day": reviews.generate("daily", previous_day),
        "agenda": agenda.generate(theme, previous_day),
        "todo": todo.generate(theme),
        "faster": fasted_metadata,
        "eater": eater.generate(theme, previous_day, fasted_metadata),
        "marriage": marriage.generate(theme),
        "kidtext": kidtext.generate(theme),
        "sponsord": sponsord.generate(theme),
        "coder": coder.generate(theme),
    }
    utilities.write_data(content_file, content)
