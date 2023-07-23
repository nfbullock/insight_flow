from jinja2 import Environment, FileSystemLoader, BaseLoader
import os

import os
from pathlib import Path

_PATH = Path(os.path.dirname(os.path.realpath(__file__)))
FILE_LOADER = FileSystemLoader(searchpath=_PATH.parent)
"""
# Assuming the input dictionary is as follows:
input_dict = {"title": "Task List", "to do": ["task 1", "task 2", "task 3"]}

# Specify the directory where your template will reside (assuming it is the current directory)
file_loader = FileSystemLoader(os.getcwd())
env = Environment(loader=file_loader)


template = env.from_string(template_string)

# Render the template with the input dictionary
output = template.render(input_dict)

# Save output to an HTML file
with open("output.html", "w") as file:
    file.write(output)

"""


def generate_from_file(template_file, params):
    environment = Environment(loader=FILE_LOADER)
    template = environment.get_template(template_file)
    return template.render(**params)


def generate(template, params):
    environment = Environment(loader=BaseLoader)
    template = environment.from_string(template)
    return template.render(**params)
