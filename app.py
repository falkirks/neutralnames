from flask import Flask
from flask_cors import CORS, cross_origin
from flask_jsonpify import jsonify
import random
lines = open('names.txt').read().splitlines()
app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def homepage():
    name = random.choice(lines)

    return name


@app.route("/api/name")
@cross_origin()
def name():
    return jsonify(name=random.choice(lines))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

