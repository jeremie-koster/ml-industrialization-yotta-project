from src.application.predict import main as prediction_pipeline

import datetime
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import sentry_sdk
import uvicorn

sentry_sdk.init(
    "https://10cea8131a31434c9e96fe6e324dcf16@o663085.ingest.sentry.io/5765736",
    traces_sample_rate=1.0,
)

app = FastAPI()

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


@app.post("/predict", response_model=Prediction)
def prediction(input: dict):

    try:
        input_df = pd.DataFrame(input, index=[0])
        csv_path = "~/sample.csv"
        input_df.to_csv(csv_path, index=False)
        result_subscription = prediction_pipeline(csv_path, run_type="api")
    except (KeyError, TypeError, ValueError) as error:
        DEFAULT_RESULT = "Error"
        result_subscription = DEFAULT_RESULT
        sentry_sdk.capture_exception(error)

    return {"predictions": result_subscription}


@app.get("/")
def index():

    return {"message": "Oui bonjour ça marche"}


if __name__ == "__main__":
    from src.config.api_config import api_config

    PORT = api_config["api"]["port"]
    HOST = api_config["api"]["host"]

    print("starting API at", datetime.datetime.now())
    uvicorn.run("src.application.server:app", host=HOST, port=PORT)
