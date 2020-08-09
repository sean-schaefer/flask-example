# Flask Example
This project assumes you're running Python 3.

First install the requirements:
``` bash
pip install -r requirements.txt
```

You should also download the corpora for TextBlob:
``` bash
python -m textblob.download_corpora
```

Then you can run the web server! For more details on `flask run` see: https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode
``` bash
FLASK_ENV=development flask run
```