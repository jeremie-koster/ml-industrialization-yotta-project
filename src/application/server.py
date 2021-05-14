import datetime

import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from src.application.predict import main as prediction_pipeline
from src.config.config import config

app = FastAPI()

PORT = config["api"]["port"]
HOST = config["api"]["host"]


class Prediction(BaseModel):
    predictions: str


@app.get("/example")
def example(input: dict):

    try:
        initial_number = input.get("question")
        answer = float(initial_number) * 2
    except (ValueError, TypeError, KeyError):
        DEFAULT_RESPONSE = 0
        answer = DEFAULT_RESPONSE
    response = {"answer": answer}
    return response


@app.get("/predict", response_model=Prediction)
def prediction(input: dict):

    input_df = pd.DataFrame(input, index=[0])
    csv_path = "~/sample.csv"
    input_df.to_csv(csv_path, index=False)

    result_subscription = prediction_pipeline(csv_path, run_type="api")
    return {"predictions": result_subscription}


@app.get("/")
def index():

    return {"message": "Oui bonjour ça marche"}


if __name__ == "__main__":
    print("starting API at", datetime.datetime.now())
    uvicorn.run("src.application.server:app", host=HOST, port=PORT)
