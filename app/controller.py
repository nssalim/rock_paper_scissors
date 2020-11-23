from app import app

@app.route('/')
def index():
    return "Welcome to Rock, Papers, Scissors!\n  The rules of the Game are:\n  Rock beats Scissors\n Scissors beats Paper\n Paper beats Rock\n Ready to play? \n What is your name?"

@app.route('/<name>') 
def greet(name): 
    return f"Hello {name}!"  