import datetime
from flask import Flask, jsonify, request

from chaos.infrastructure.config.config import config


app = Flask(__name__)
PORT = config["api"]["port"]
HOST = config["api"]["host"]


@app.route("/example", methods=["GET"])
def example():
    try:
        initial_number = request.get_json()["question"]
        answer = float(initial_number)*2
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    response = {"answer": answer}
    return jsonify(response)


if __name__ == "__main__":
    print("starting API at", datetime.datetime.now())
    app.run(debug=False, host=HOST, port=PORT)
