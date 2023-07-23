import utilities, template, generative_AI

from . import prompts

FILES = {
    "previous": "data/previous_themes.json",
    "principles": "data/principles.json",
}


def generate(gai, review_metadata):
    previous_metadata = utilities.read_data(FILES["previous"])
    principles = utilities.read_data(FILES["principles"])
    user_prompt_text = template.generate_from_file(
        "daily_motif/user_prompt.j2",
        params={
            "previous_themes": previous_metadata.get("themes"),
            "principles": principles,
            "comments": review_metadata.get("daily_motif", {}).get("comments"),
        },
    )
    messages = [
        generative_AI.system_prompt(prompts.main_system),
        generative_AI.user_prompt(user_prompt_text),
    ]
    gai.submit_prompt("theme", messages, load_response=True)


def review():
    return {}
