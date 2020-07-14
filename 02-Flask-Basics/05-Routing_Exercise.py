from flask import Flask
app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return '<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    if name[-1] == 'y':
        result = name[:-1] + 'iful'
    else:
        result = name + 'y'
    return '<h1>Hi ' + name + '! Your puppylatin name is ' + result + '</h1>'

if __name__ == '__main__':
    app.run(debug=True)
