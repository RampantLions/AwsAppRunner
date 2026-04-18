import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Hello from AWS App Runner!", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})
