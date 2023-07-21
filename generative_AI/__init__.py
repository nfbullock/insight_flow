import openai

class Chat:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.models = {}
    
    def create_model(self, model_name):
        self.models[model_name] = {
            'chat_log': {}
        }
    
    def delete_model(self, model_name):
        if model_name in self.models:
            del self.models[model_name]
    
    def submit_prompt(self, model_name, prompt, prompt_key):
        if model_name not in self.models:
            print(f"Model '{model_name}' does not exist.")
            return
        
        model = self.models[model_name]
        model['chat_log'].append(f"user: {prompt}\n")
        model['chat_log'].update(

        )
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt="".join(model['chat_log']),
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
            echo=True
        )
        
        model['chat_log'].append(f"AI: {response.choices[0].text}\n")
        
        return response.choices[0].text.strip()
