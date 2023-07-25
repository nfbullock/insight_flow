import config
import generative_AI
import template
import utilities

from . import prompts

FILES = {
    "previous": "data/previous_themes.json",
    "principles": "data/principles.json",
}

STUB_THEME = {
    "corollary": "The Universe in its entirety is a celebration of Yin and Yang. This theme beckons you towards perceiving not just grand cosmic interplays but also the minutiae of your everyday existence through this lens. Each activity, every interaction, every introspection \u2013 offers a dance of dualities to detect, analyze, and integrate into your consciousness while maintaining harmony.",
    "description": "Anchored in the ancient Chinese philosophy of Taoism, the concept of Yin and Yang offers a profound framework to perceive and interpret our daily life. Yin and Yang represent the two complementary forces existent in all aspects of the universe, and their interaction gives birth to the reality we perceive.\nYin corresponds to dark, moon, passive, feminine, downward, cold, and even numbers, while Yang is defined by light, sun, active, masculine, upward, hot, and odd numbers. Neither is superior or inferior, but rather, they depend on each other to exist, like two sides of the same coin.\nLet this theme guide your actions and reflections today. Every interaction, every activity, every thought\u2014attempt to identify the Yin and Yang components within them. Acknowledge that within every success (Yang), there is diligence and failure (Yin). Recognize that the tranquility and solitude (Yin) you enjoy is sometimes disrupted by social commitments (Yang). Life is a perpetual dance of these dualities, an intertwined equilibrium where Yin and Yang give rise to each other, control each other, and transform into each other.\nThis recognition, integrates seamlessly with Aristotle's 'Golden Mean' from Western Philosophy, reinforcing a balance rather than extremities. Counterbalancing the virtues to not fall into vices, reflects the ebb and flow of Yin and Yang. Extending this harmonizing principle onto Sartre's Existentialism, we comprehend that while our freedom (Yang) allows us to make choices, it also brings consequence and responsibility (Yin).\nYour day, viewed through the lens of 'Harmony in Duality,' can be an intellectual exploration of life's intrinsic polarities and the transformative dynamics of Yin and Yang\u2014An encouragement for perpetual mindfulness. At every juncture, you are empowered to harmonize Yin and Yang, to conjure a reality that best serves your intellectual, spiritual and emotional well-being.",
    "extended_encapsulation": "Harmony in Duality invites you to perceive every facet of your daily life through a Taoist lens, seeking the balance between Yin and Yang, exemplifying the interconnected nature of the world and realizing the path of moderation, simplicity, and mindfulness.",
    "title": "Harmony in Duality: A Dance between Yin and Yang",
}


def generate(gai, review_metadata):
    previous_metadata = utilities.read_data(FILES["previous"])
    principles = utilities.read_data(FILES["principles"])
    parameters = {
        "previous_themes": previous_metadata.get("themes"),
        "principles": config.principles,
    }
    user_prompt_text = template.generate(prompts.user, params=parameters)
    messages = [
        generative_AI.system_prompt(prompts.system),
        generative_AI.user_prompt(user_prompt_text),
    ]
    gai.submit_prompt("theme", messages, load_response=True)
    return gai.theme.content
    # gai.theme.content = STUB_THEME


def review():
    return {}
