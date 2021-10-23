from sample_sklearn.base import HousingDataType
from sample_sklearn.errors import InvalidDataError
from sklearn.datasets import fetch_california_housing, load_boston
from sklearn.linear_model import LinearRegression
from sklearn.base import BaseEstimator
import numpy as np
from typing import Tuple
import pickle
from pathlib import Path


def retrieve_data(data_type: HousingDataType) -> Tuple[np.ndarray, np.ndarray]:
    """Method to retrieve dataset. Returns a tuple of attributes and target values
    """
    if data_type == HousingDataType.CALIFORNIA:
        return fetch_california_housing(return_X_y=True)
    elif data_type == HousingDataType.BOSTON:
        return load_boston(return_X_y=True)
    else:
        raise InvalidDataError(
            data_type=data_type,
            message="Requested invalid data."
        )


def train_linear_regression(
    X: np.ndarray, y: np.ndarray
) -> BaseEstimator:
    """ Method to train a linear regression model
    """
    classifier = LinearRegression()
    return classifier.fit(X, y)


def save_model(model: BaseEstimator, path: str) -> None:
    """ Save model to the specified location
    """
    Path(path).mkdir(parents=True, exist_ok=True)
    class_name = type(model).__name__
    final_path = f"{path}/{class_name}.pkl"
    with open(final_path, "wb") as f:
        pickle.dump(model, f)


def main():
    X, y = retrieve_data(HousingDataType.CALIFORNIA)
    model = train_linear_regression(X, y)
    save_model(model, "./model")
    print("SUCCESS")

if __name__=="__main__":
    main()
