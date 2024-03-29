'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def general():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>GPT Demo</h1>
        
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <br>
        <a href="{url_for('index')}">Index</a>
        <br>
        <a href="{url_for('about')}">About page</a>
        <br>
        <a href="{url_for('team')}">Team page</a>
        
    '''

@app.route("/about")
def about():
    return '''
    <h1>About Page</h1>
    <p>This is a demo of a web app which uses GPT to answer dino related questions. :).<br>
    Check out our <a href="https://github.com/noammolloy/CS103aSpr23TeamProjects">Github</a> page for more information.
    </p>
    ''' 

@app.route("/index")
def index():
    return '''
    <h1>Index</h1>
    <p>
    <a href="http://127.0.0.1:5001/Noam">Noam</a><br>
    <a href="http://127.0.0.1:5001/Zared">Zared</a><br>
    <a href="http://127.0.0.1:5001/Sydney">Sydney</a><br>
    <a href="http://127.0.0.1:5001/Jingyi">Jingyi</a>
    </p>
    ''' 

@app.route("/Noam", methods=['GET', 'POST'])
def route_noam():
    if request.method == 'GET':
        return '''
        <form method="POST">
        This prompt will change the following code's variables into dino-themed variables: <input type="text" name="prompt"><br>
        <input type="submit">
        </form>
        '''
    elif request.method == 'POST':
        prompt = str(request.form['prompt'])
        return gptAPI.dino_code_variables(prompt)

    else:
        return 'unknown HTTP method: '+str(request.method)
    
@app.route("/Zared", methods=['GET', 'POST'])
def route_zared():
    if request.method == 'GET':
        return '''
        <form method="POST">
        Enter the name of a new dinosaur: <input type="text" name="prompt"><br>
        <input type="submit">
        </form>
        '''
    elif request.method == 'POST':
        prompt = str(request.form['prompt'])
        return gptAPI.dino_create(prompt)

    else:
        return 'unknown HTTP method: '+str(request.method)
    
@app.route("/Sydney", methods=['GET', 'POST'])
def route_sydney():
    if request.method == 'GET':
        return '''
        <form method="POST">
        Enter input keywords about dinosaurs: <input type="text" name="prompt"><br>
        <input type="submit">
        </form>
        '''
    elif request.method == 'POST':
        prompt = str(request.form['prompt'])
        return gptAPI.dino_story(prompt)

    else:
        return 'unknown HTTP method: '+str(request.method)
    
@app.route("/Jingyi", methods=['GET', 'POST'])
def route_jingyi():
    if request.method == 'GET':
        return '''
        <form method="POST">
        Enter a prompt you would like to be changed into dino-speak: <input type="text" name="prompt"><br>
        <input type="submit">
        </form>
        '''
    elif request.method == 'POST':
        prompt = str(request.form['prompt'])
        return gptAPI.dino_convo(prompt)

    else:
        return 'unknown HTTP method: '+str(request.method)


@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
    
@app.route('/team')
def team():
    return '''
    <h1>Team page</h1>
    <ul>
      <li><strong>Noam: </strong></li><br>
            Created the dino_code_variables()
            <br> - Takes in code, and returns the same code with dinosaur themed variables
      <br>
      <li><strong>Sydney: </strong></li><br>
            Sydney is a sophomore majoring in Computer Science and Environmental Studies. She created the dino_story()
            <br> - It takes in input keywords, and returns a short story about dinosaurs with those words.
        <br>
      <li><strong>Jingyi: </strong></li><br>
            Jingyi is a sophomore majoring cs and creative writing. She created dino_convo()
            <br> - It takes in text, and returns it, written as if directed toward a dinosaur!<br>
      <li><strong>Zared: </strong></li><br>
            Zared is a sophomore majoring in computer science. He created dino_create()
            <br> It takes in key words, and creates a dinosuar!<br>
    </ul>
    '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)