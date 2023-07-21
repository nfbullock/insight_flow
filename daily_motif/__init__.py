import utilities, templater

FILES = {
    "previous": "data/previous_themes.json",
    "principles": "data/principles.json"
}

def generate(review_metadata):
    previous_metadata = utilities.read_data(FILES["previous"])
    principles = utilities.read_data(FILES["principles"])
    prompt = templater.generate(
        "prompt.j2",
        params={
            "previous_themes": previous_metadata["themes"],
            "principles": principles,
            "comments": review_metadata["daily_motif"].get("comments")
        }
    )

def review():
    return {}
