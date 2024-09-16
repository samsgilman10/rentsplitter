from flask import Flask
import redis

app = Flask(__name__)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@app.route("/")
def hello_world():
    if r.exists('key'):
        value = r.get('key')
    else:
        value = r.set('key', 0)
    r.incr('key')
    return {
        "value": int(value)
    }