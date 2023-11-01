from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def home():
    joke = None
    if request.method == 'POST':
        response = requests.get('https://api.chucknorris.io/jokes/random')
        if response.status_code == 200:
            response_dict = response.json()
            joke = response_dict.get('value')
    return render_template('home.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)