from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def array():
  return jsonify([8, 6, -2, 2, 4, 17, 256, 1024, -17, -19])
