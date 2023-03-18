'''
Demo code for interacting with GPT-3 in Python.

To run this you need to 
* first visit openai.com and get an APIkey, 
* which you export into the environment as shown in the shell code below.
* next create a folder and put this file in the folder as gpt.py
* finally run the following commands in that folder

On Mac
% pip3 install openai
% export APIKEY="......."  # in bash
% python3 gpt.py

On Windows:
% pip install openai
% $env:APIKEY="....." # in powershell
% python gpt.py
'''
import openai

class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
        openai.api_key = apikey #os.environ.get('APIKEY')

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self,prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
    # Noam
    def dino_code_variables(self, prompt):
        prompt = 'Change the variable names in the following code to be dinosaur themed: ' + prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    # Jingyi
    def dino_convo(self, prompt):
        prompt = 'Change the following text to be written as if you are talking to a dinosaur' + prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

        
    
    # Sydney
    def dino_story(self, prompt):
        prompt = 'Create a short story using these input keywords about dinosaurs: ' + prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response
    
        
    # Zared
    def dino_create(self, prompt):
        prompt = 'Create and describe a new dinosaur with the name ' + prompt
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

if __name__=='__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    # print(g.getResponse("what does openai's GPT stand for?"))
    print(g.dino_story("pizza, cake, bbq, party"))
    print(g.dino_code_variables("""num1 = 5
                                \nnum2 = 10
                                \nsum = num1 + num2
                                \nprint('The sum of', num1, 'and', num2, 'is', sum)
                                """))
    print(g.dino_create("Bobby"))
    print(g.dino_convo("Good morning, I am currently working on some homework. But I am very very hungry! Lunch time."))




