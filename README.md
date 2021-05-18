# Cloud deployment project

Project n°3 - Yotta Academy 2021 - Machine Learning Engineer bootcamp

Authors: Olivier COLLIER & Jérémie KOSTER

The goal of this project is to deploy a machine learning model (from project n°1). To achieve that we:
- Wrap the model in a REST API (FastAPI) and expose it through an endpoint
- Set up 3 environments (develop, staging, master)
- Create a GitLab CI/CD that automatically :
    - runs unit and functional tests
    - build a Docker image
    - deploy it on a Kubernetes cluster on GCP
