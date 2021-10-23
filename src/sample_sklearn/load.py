import pickle
from sklearn.base import BaseEstimator


def load_model(path: str= "./model/LinearRegression.pkl") -> BaseEstimator:
    with open(path, "rb") as f:
        model = pickle.load(f)
    
    return model
