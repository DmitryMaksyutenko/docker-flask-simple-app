from flask import Flask

import redis


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/')
def index():
    cache.set('key', 'value1')
    value = cache.get('key').decode('utf8')
    return f'The main page {value}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
