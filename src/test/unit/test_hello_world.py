import os
from src.config.base import MODELS_DIR


def test_street_fighter():
    assert "guile" > "bison"


def test_model_file_exists():
    model = os.path.join(MODELS_DIR, "ml_model.pkl")
    assert os.path.isfile(model)


if __name__ == "__main__":
    test_model_file_exists()
