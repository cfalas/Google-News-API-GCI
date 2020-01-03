# Google News API Frontend

Shows the 20 latest News about Linux, Open Source and Android
Uses the [newsapi.org API](https://newsapi.org/s/google-news-api)

## Installation

In order to install, create a virtual environment using `python -m venv env` and activate it using `source env/bin/activate`
Install the dependencies using `pip install -r requirements.txt`

## Usage

Obtain an API key from [newsapi.org](https://newsapi.org/s/google-news-api)
Run the command `export NEWS_API_KEY=<api_key>`, where you should replace `<api_key>` with the API key you obtained.
Run the server: `python application.py`
A link will appear (http://127.0.0.1:5000). If you open it in your browser, you should see the latest news.
