from flask import Flask
import os
import requests
import json
from flask import render_template
app = Flask(__name__)

API_KEY = os.environ['NEWS_API_KEY']

# Queries the Google News API to get more recent news about Linux, Open Source, and Android
# Returns a JSON list, which contains the details for each article
def get_results():
    url = 'https://newsapi.org/v2/everything'
    res = requests.get(url, {'apiKey':API_KEY, 'q': 'Android OR Open-Source OR Linux'})
    return json.loads(res.content)['articles']


@app.route('/')
def show_results():
    return render_template('show_items.html', articles=get_results())
if __name__ == '__main__':
    app.run(debug=True)
