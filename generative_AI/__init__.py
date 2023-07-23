import pprint
import json

import openai
import pydantic
import yaml


class Context(pydantic.BaseModel):
    model: str
    content: dict = {}
    has_sub_prompts: bool = False


class Chat:
    def __init__(self, api_key):
        openai.api_key = api_key

    def create_model(self, chat, model="gpt-4", sub_prompts=False):
        setattr(self, chat, Context(model=model, has_sub_prompts=sub_prompts))

    def submit_prompt(
        self,
        chat,
        prompt,
        sub_prompt_key: str = None,
        load_response: bool = False,
    ):
        if not hasattr(self, chat):
            self.create_model(chat)
        current_context = getattr(self, chat)
        """
        response = openai.ChatCompletion.create(
            model=current_context.model,
            messages=prompt,
        )
        content = response["choices"][0]["message"]["content"]
        """
        content = "{}"
        if load_response:
            content = yaml.safe_load(content)
        print(current_context)
        if current_context.has_sub_prompts:
            current_context.content[sub_prompt_key] = content
        else:
            current_context.content = content


def system_prompt(text):
    return {"role": "system", "content": text}


def user_prompt(text):
    return {"role": "user", "content": text}
