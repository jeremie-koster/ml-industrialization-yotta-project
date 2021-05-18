from src.application.server import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_predict():
    endpoint = "predict"
    headers = {"Content-Type": "application/json"}
    data = {
        "DATE": "2010-02-24",
        "AGE": 0,
        "JOB_TYPE": "Admin",
        "STATUS": "Marié",
        "EDUCATION": "Primaire",
        "HAS_DEFAULT": "No",
        "BALANCE": 0,
        "HAS_HOUSING_LOAN": "No",
        "HAS_PERSO_LOAN": "Yes",
        "CONTACT": "Portable",
        "DURATION_CONTACT": 99,
        "NB_CONTACT": 2,
        "NB_DAY_LAST_CONTACT": 86,
        "NB_CONTACT_LAST_CAMPAIGN": 5,
        "RESULT_LAST_CAMPAIGN": "Echec",
    }
    response = client.get(f"/{endpoint}", json=data, headers=headers)
    results = response.json()
    assert results["predictions"] == "A souscrit"
