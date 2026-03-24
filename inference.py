import joblib
from training import MODEL_FILE

model = None


def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_FILE)
    return model


def predict(input_data: dict):
    model = load_model()
    X = [
        [
            input_data["sepal_length"],
            input_data["sepal_width"],
            input_data["petal_length"],
            input_data["petal_width"],
        ]
    ]
    prediction_index = model.predict(X)[0]
    return str(prediction_index)
