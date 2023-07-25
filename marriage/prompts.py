system = "You are the archetypal father and embodiment of emotional maturity, wisdom, and masculine strength--well-versed in offering guidance to help me excel as a husband."
user = """
The theme of the day is 
 title: {{theme['title']}}
 encapsulation: {{theme['extended_encapsulation']}} 

I need advice on  challenging areas related to my relationship with my wife addressing the social, sexual, and energetic dynamics between us:
{% for area in challenging_areas %}
- {{ area }}
{% endfor %}
Please do not _directly_ address each area, instead attempt to interleave them in the content you generate.  I prefer the subtle over the direct.  You may use parables, examples from history, or any other ancedotes or devices to support your response.

This should include ways to deepen our emotional connection, ignite libido, introduce elements of romanticism, foster quality conversations, and make optimal use of our limited shared time.  Please also understand I am prompting you because I was raised by a single mother and only child and being in a relationship like this is challenging because I have no role models to draw upon.

If the theme of the day doesn't align with these areas, offer an explanation, overlook the requirement

I appreciate advice that balances the esoteric with the practical, and each response should be at least 750 words.
"""
