from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Metric to track endpoint calls
HELLO_COUNT = Counter('hello_world_requests', 'Number of Hello World requests')

@app.route("/")
def hello_world():
    HELLO_COUNT.inc()
    return jsonify({"message": "Hello World!"})

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
