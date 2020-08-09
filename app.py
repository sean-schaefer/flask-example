#!/usr/bin/env python
from flask import Flask, redirect, url_for, request
from nltk import ngrams, FreqDist

app = Flask(__name__)


@app.route('/', methods=['GET'])
def serve():
    return redirect(url_for('static', filename='index.html'))


@app.route('/json', methods=['POST'])
def json():
    req = request.get_json()

    # Find trigrams
    trigrams_dict = dict(FreqDist(ngrams(req['data'].split(), 3)))
    counts = {' '.join(k): v for k, v in iter(trigrams_dict.items())}
    return {'counts': counts}, 200


if __name__ == '__main__':
    app.run()
