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
<<<<<<< HEAD
# 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
=======
# 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
>>>>>>> d24f36a586645cf9b70dd607dfdb5122ca0e7347

class GPT():
    ''' make queries to gpt from a given API '''
    def __init__(self,apikey):
        ''' store the apikey in an instance variable '''
        self.apikey=apikey
        # Set up the OpenAI API client
<<<<<<< HEAD
        openai.api_key = "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" #os.environ.get('APIKEY')
=======
        openai.api_key = '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'
 #os.environ.get('APIKEY')
>>>>>>> 6730a5e03122d6a7e30976c8f5c868bf853913aa

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
    
    def dino_code_variables(self, prompt):
        prompt = 'Change the variables in the following code to be dinosaur themed: ' + prompt
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
<<<<<<< HEAD
    g = GPT(os.environ.get("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"))
=======
<<<<<<< HEAD
    g = GPT(os.environ.get("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"))
=======
    g = GPT(os.environ.get("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"))
>>>>>>> 6730a5e03122d6a7e30976c8f5c868bf853913aa
>>>>>>> d24f36a586645cf9b70dd607dfdb5122ca0e7347
    print(g.getResponse("what does openai's GPT stand for?"))