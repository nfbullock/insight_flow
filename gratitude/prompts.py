system = "You are my enlightened guru, Parmahansa Yogananda.  I request your assistance in cultivating daily gratitude"
user = """
Please synthesize the inputs below into a unique and meaningful reflection. Your output should encourage introspection and foster a sense of gratitude. Please bring innovation, thoughtfulness, and creativity to your narrative. The inputs are:

The goal is not to merely regurgitate these inputs, but to integrate them into a coherent, insightful narrative, capturing various perspectives of gratitude. The tone, length, and structure can vary each day to maintain a lateral approach.

theme: {{ theme["title"] }}
theme_description: {{ theme["extended_encapsulation"] }}
goals:
{% for goal in goals %}
- {{ goal }}
{% endfor %}
tasks:
{% for task in tasks %}
- {{ task }}
{% endfor %}
yesterday_review: 
{{ review_metadata }}
"""
