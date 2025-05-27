from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask(__name__)
GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')  # configurar no Render

@app.route('/', methods=['GET', 'POST'])
def index():
    gifs = []
    query = None
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            url = 'https://api.giphy.com/v1/gifs/search'
            params = {
                'api_key': GIPHY_API_KEY,
                'q': query,
                'limit': 5,
                'rating': 'g'
            }
            resp = requests.get(url, params=params)
            data = resp.json()
            gifs = [item['images']['downsized_medium']['url'] for item in data.get('data', [])]
    return render_template('index.html', gifs=gifs, query=query)

if __name__ == '__main__':
    app.run(debug=True)