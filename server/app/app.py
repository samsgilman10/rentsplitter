from flask import Flask, jsonify
import redis
import os
from flask_cors import CORS

FRONTEND_URL = os.getenv('FRONTEND_URL')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

app = Flask(__name__)
CORS(app, origins=[FRONTEND_URL])

pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)
r = redis.Redis(connection_pool=pool)


@app.route("/")
def hello_world():
    if r.exists('key'):
        value = r.get('key')
    else:
        value = r.set('key', 0)
    r.incr('key')
    response = jsonify({'value': int(value)})
    return response