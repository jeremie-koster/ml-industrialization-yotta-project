import os
import src


def test_street_fighter():
    assert "guile" > "bison"


def test_model_file_exists():
    model = os.path.join(src.__path__[0], "../models/ml_model.pkl")
    assert os.path.isfile(model)


if __name__ == "__main__":
    test_model_file_exists()
