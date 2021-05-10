import src.domain.build_features

import numpy as np
import os


def test_street_fighter():
    assert "guile" > "bison"


def test_model_file_exists():
    model = os.path.join(src.__path__[0], "../models/ml_model.pkl")
    assert os.path.isfile(model)


def test_clip_transformer():
    data = 5 + np.random.randn(100)
    a_min = 0
    a_max = 6
    transformer = ClipTransformer(a_min, a_max)
    transformed_data = transformer.fit_transform(data)
    assert all(transformed_data >= a_min / (a_max - a_min)) & all(transformed_data <= a_max / (a_max - a_min))


def test_extract_category_transformer():
    data = np.array(['a'] * 5 + ['b'] * 4 + ['c'] * 3)
    transformer = ExtractCategoryTransformer()
    transformed_data = transformer.fit_transform(data)
    assert all(transformed_data == data.mode()[0])


def test_age_transformer1():
    data = 40 + 5 * np.random.randn(100)
    transformer = AgeTransformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data[0, :]])


def test_age_transformer2():
    data = 40 + 5 * np.random.randn(100)
    transformer = AgeTransformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data[1, :]])


def test_age_transformer3():
    data = 40 + 5 * np.random.randn(100)
    transformer = AgeTransformer()
    transformed_data = transformer.fit_transform(data)
    assert np.isclose((np.mean(transformed_data[2, :]), 0, 1e-5)) & np.isclose(np.std(transformed_data[2, :]), 1, 1e-5)


def test_logical_transformer():
    data = np.random.randint(0, 2, (100, 2))
    transformer = LogicalOrTransformer()
    transformed_data = transformer.fit_transform(data)
    assert all([x in [0, 1] for x in transformed_data])


def test_impute_missing_eco_data():
    data = [np.nan, 1, 2, np.nan, 4, np.nan]
    transformed_data = impute_missing_eco_data(data)
    assert not any(transformed_data.isnull())


def test_correct_wrong_entries():
    data = np.arange(10)
    corrections = {0: 'a', 1: 'b'}
    transformed_data = correct_wrong_entries(data, corrections)
    assert all(transformed_data not in list(corrections.keys())


#if __name__ == "__main__":
#    test_model_file_exists()
