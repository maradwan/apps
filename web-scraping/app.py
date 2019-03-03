from random import randint
from flask import Flask
import requests
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)
app.secret_key = 'abcde'
cache = SimpleCache()


url = 'https://raw.githubusercontent.com/maradwan/apps/master/fortune_of_the_day.json'

def get_my_item():
    rv = cache.get('msg')
    if rv is None:
        data = requests.get(url).json()
        length = len(data)
        random = randint(0,length-1)
        rv = (data[random]['message'])
        cache.set('msg', rv, timeout=10)
    return rv

@app.route('/')
def home():
    return get_my_item()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
