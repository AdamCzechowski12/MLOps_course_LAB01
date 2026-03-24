from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import predict

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_endpoint(request: PredictRequest) -> PredictResponse:
    prediction = predict(request.model_dump())
    return PredictResponse(prediction=prediction)
