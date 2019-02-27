from flask import Flask
from flask_cors import CORS, cross_origin
import random
lines = open('names.txt').read().splitlines()
app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def homepage():
    name = random.choice(lines)

    return name

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

