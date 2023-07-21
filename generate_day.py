import utilities

if __name__ == "__main__":
    previous_day = reviews.fetch("yesterday")
    theme = daily_motif.generate(previous_day)
    fasted_metadata = faster.generate(previous_day)
    content = {
        "theme": theme,
        "gratitude": gratitude.generate(theme),
        "previous_day": reviews.generate("daily", previous_day),
        "agenda": agenda.generate(theme, previous_day),
        "todo": todo.generate(theme),
        "faster": fasted_metadata,
        "eater": eater.generate(previous_day, fasted_metadata),
        "marriage": marriage.generate(theme),
        "kidtext": kidtext.generate(theme),
        "sponsord": sponsord.generate(theme),
        "coder": coder.generate(theme),
        "wisdom": wisdom.generate(theme, previous_day)
    }
    utilities.write_data(content_file, content)
