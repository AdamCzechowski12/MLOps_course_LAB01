from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

MODEL_FILE = "iris_model.joblib"


def load_data():
    data = load_iris()
    X, y, target_names = data.data, data.target, data.target_names
    return X, y, target_names


def train_model():
    X, y, _ = load_data()
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


def save_model(model):
    joblib.dump(model, MODEL_FILE)
    print(f"Model zapisany w {MODEL_FILE}")


if __name__ == "__main__":
    model = train_model()
    save_model(model)
