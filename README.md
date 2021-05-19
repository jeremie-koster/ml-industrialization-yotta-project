# Cloud deployment project

Project n°3 - Yotta Academy 2021 - Machine Learning Engineer bootcamp

Authors: Olivier COLLIER & Jérémie KOSTER

The goal of this project is to deploy a machine learning model (from project n°1). To achieve that we:
- Wrap the model in a REST API (FastAPI) and expose it through an endpoint (`/predict`)
- Set up 3 environments (develop, staging, master)
- Create a GitLab CI/CD that automatically :
    - runs unit and functional tests
    - build a Docker image
    - deploy it on a Kubernetes cluster on GCP

# How to use the deployed API

The API is exposed with Kubernetes on GCP at this address: `35.190.208.127:5000`. You should use the `/predict` endpoint to make a prediction with the model.

# Installation

To install the project and the dependencies, follow these steps:

    git clone git@gitlab.com:yotta-academy/mle-bootcamp/projects/ml-prod-projects/project-3-winter-2021/chaos-2.git
    cd chaos-2/
    python -m venv .venv
    . ./activate.sh
    make install

# Run the tests

To run the unit tests:

     pytest src/test/unit

To run the functional test:

    pytest src/test/functional

# Documentation

A short documentation of our endpoint is available [here](https://app.swaggerhub.com/apis/Yotta-Academy/project-3_yotta/1.0.0).

# How to use the API locally

We chose not to commit the configuration file related to the API (it contains the IP address and the port). We have loaded on GCP through a configMap that we mount on the pod.

Despite that, you can run the API locally by running: `make run`. The API now runs on http://0.0.0.0:5000

Once the API is running locally, you can test it with a `curl` command like this one:
````bash
curl --location --request GET '0.0.0.0:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"DATE":"2010-02-24",
"AGE":20,
"JOB_TYPE":"Admin",
"STATUS":"Marié",
"EDUCATION":"Primaire",
"HAS_DEFAULT":"No",
"BALANCE":2000,
"HAS_HOUSING_LOAN":"No",
"HAS_PERSO_LOAN":"Yes",
"CONTACT":"Portable",
"DURATION_CONTACT":99,
"NB_CONTACT":2,
"NB_DAY_LAST_CONTACT":86,
"NB_CONTACT_LAST_CAMPAIGN":5,
"RESULT_LAST_CAMPAIGN":"Echec"
}'
```
