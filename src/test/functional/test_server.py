from src.application.server import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_predict():
    endpoint = "predict"
    headers = {"Content-Type": 'application/json'}
    data = {"DATE":"2010-02-24",\
            "AGE": 0,\
            "JOB_TYPE": "Admin",\
            "STATUS": "Marié",\
            "EDUCATION": "Primaire",\
            "HAS_DEFAULT": "No",\
            "BALANCE": 0,\
            "HAS_HOUSING_LOAN": "No",\
            "HAS_PERSO_LOAN": "Yes",\
            "CONTACT": "Portable",\
            "DURATION_CONTACT": 99,\
            "NB_CONTACT": 2,\
            "NB_DAY_LAST_CONTACT": 86,\
            "NB_CONTACT_LAST_CAMPAIGN": 5,\
            "RESULT_LAST_CAMPAIGN": "Echec"}
    response = client.post(f"/{endpoint}", json=data, headers=headers)
    results = response.json()
    assert results['predictions'] == "A souscrit"


#def test_example1():
#    endpoint = "example"
#    url = f"http://{host}:{port}/{endpoint}"
#    headers = {"Content-type": "application/json"}
#
#    data = {"question": 2}
#
#    response = requests.get(url=url, json=data, headers=headers)
#    results = response.json()
#    assert results["answer"] == data["question"]*2

#def test_example2():
#    endpoint = "example"
#    url = f"http://{host}:{port}/{endpoint}"
#    headers = {"Content-type": "application/json"}
#    data = {"question": "a"}
#    response = requests.get(url=url, json=data, headers=headers)
#    results = response.json()
#    assert results["answer"] == 0


#def test_example3():
#    endpoint = "example"
#    url = f"http://{host}:{port}/{endpoint}"
#    headers = {"Content-type": "application/json"}
#    data = {"wrong_field": "a"}
#    response = requests.get(url=url, json=data, headers=headers)
#    results = response.json()
#    assert results["answer"] == 0