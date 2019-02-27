from flask import Flask
import random
lines = open('names.txt').read().splitlines()
app = Flask(__name__)

@app.route('/')
def homepage():
    name = random.choice(lines)

    return name

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

