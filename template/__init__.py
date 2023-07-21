from jinja2 import Environment, FileSystemLoader
import os

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