import datetime
from flask import Flask, jsonify, request
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

from src.infrastructure.config.config import config


# app = Flask(__name__)
app = FastAPI()

PORT = config["api"]["port"]
HOST = config["api"]["host"]

class Prediction(BaseModel):
    predictions: str


@app.post("/example")
def example(input: dict):
    
    try:
        initial_number = input.get("question")
        answer = float(initial_number)*2
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    response = {"answer": answer}
    return response


@app.post("/predict")
def prediction(input: dict):

    try:
        balance = input.get("balance")
        answer = float(balance)*2
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    
    return {"predictions": answer}

@app.get("/")
def index():
    return {"message": "Oui bonjour ça marche"}

if __name__ == "__main__":
    print("starting API at", datetime.datetime.now())
    uvicorn.run("src.application.server:app", host=HOST, port=PORT)
