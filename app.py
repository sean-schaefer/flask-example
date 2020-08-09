#!/usr/bin/env python
from flask import Flask, redirect, url_for, request
from textblob import TextBlob

app = Flask(__name__)


# The serve method is what allows the web server to give the index.html and index.js to the browser
# You shouldn't need to change this
@app.route('/', methods=['GET'])
def serve():
    return redirect(url_for('static', filename='index.html'))


@app.route('/json', methods=['POST'])
def json():
    # Get JSON (body) from web browser (client)
    req = request.get_json()

    # Processing starts HERE
    print('Processing...')
    catHatTextBlob = TextBlob(req['data'])
    sentences = [{
        'sentence': sentence.raw,
        'polarity': sentence.polarity,
        'sentiment': sentence.sentiment
    } for sentence in catHatTextBlob.sentences]
    # Done with processing

    # Return JSON (response) to web browser
    # Shouldn't need to change this
    return {'sentences': sentences}, 200


if __name__ == '__main__':
    app.run()
