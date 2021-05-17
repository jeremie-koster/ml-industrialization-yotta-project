import src.config.base as base
import src.domain.build_features as bf
import src.domain.cleaning as cl

import numpy as np
import os
import pandas as pd


def test_model_file_exists():
    model = os.path.join(base.REPO_DIR, "models/ml_model.pkl")
    assert os.path.isfile(model)


def test_clip_transformer():
    data = pd.DataFrame(5 + np.random.randn(10))
    a_min = 0
    a_max = 6
    transformer = bf.ClipTransformer(a_min, a_max)
    transformed_data = transformer.fit_transform(data)
    print(data)
    print(transformed_data)
    assert (
        transformed_data.ne(a_min / (a_max - a_min)).all()[0]
        & transformed_data.le(a_max / (a_max - a_min)).all()[0]
    )


def test_extract_category_transformer():
    data = pd.DataFrame(np.array(["a"] * 5 + ["b"] * 4 + ["c"] * 3))
    transformer = bf.ExtractCategoryTransformer("a")
    transformed_data = transformer.fit_transform(data)
    assert transformed_data.isin([0, 1]).all()[0]


def test_age_transformer1():
    data = pd.DataFrame(40 + 5 * np.random.randn(100))
    transformer = bf.age_transformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data[:, 0]])


def test_age_transformer2():
    data = pd.DataFrame(40 + 5 * np.random.randn(100))
    transformer = bf.age_transformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data[:, 1]])


def test_age_transformer3():
    data = pd.DataFrame(40 + 5 * np.random.randn(10))
    transformer = bf.age_transformer()
    transformed_data = transformer.fit_transform(data)
    assert np.isclose(np.mean(transformed_data[:, 2]), 0, 1e-5) & np.isclose(
        np.std(transformed_data[:, 2]), 1, 1e-5
    )


def test_logical_transformer():
    data = np.random.randint(0, 2, (100, 2))
    transformer = bf.LogicalOrTransformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data])


def test_clip_transformer():
    data = pd.DataFrame(5 + np.random.randn(10))
    a_min = 0
    a_max = 6
    transformer = bf.ClipTransformer(a_min, a_max)
    transformed_data = transformer.fit_transform(data)
    print(data)
    print(transformed_data)
    assert (
        transformed_data.ne(a_min / (a_max - a_min)).all()[0]
        & transformed_data.le(a_max / (a_max - a_min)).all()[0]
    )


def test_extract_category_transformer():
    data = pd.DataFrame(np.array(["a"] * 5 + ["b"] * 4 + ["c"] * 3))
    transformer = bf.ExtractCategoryTransformer("a")
    transformed_data = transformer.fit_transform(data)
    assert transformed_data.isin([0, 1]).all()[0]


def test_age_transformer1():
    data = pd.DataFrame(40 + 5 * np.random.randn(100))
    transformer = bf.age_transformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data[:, 0]])


def test_age_transformer2():
    data = pd.DataFrame(40 + 5 * np.random.randn(100))
    transformer = bf.age_transformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data[:, 1]])


def test_age_transformer3():
    data = pd.DataFrame(40 + 5 * np.random.randn(10))
    transformer = bf.age_transformer()
    transformed_data = transformer.fit_transform(data)
    assert np.isclose(np.mean(transformed_data[:, 2]), 0, 1e-5) & np.isclose(
        np.std(transformed_data[:, 2]), 1, 1e-5
    )


def test_logical_transformer():
    data = pd.DataFrame(np.random.randint(0, 2, (100, 2)))
    transformer = bf.LogicalOrTransformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data])


def test_impute_missing_eco_data():
    data = pd.DataFrame([np.nan, 1, 2, np.nan, 4, np.nan])
    transformed_data = cl.impute_missing_eco_data(data)
    assert not any(transformed_data.isnull())
