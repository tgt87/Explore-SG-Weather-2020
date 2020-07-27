from fastapi import FastAPI
from model import PredictionInput, PredictionOutput
import predict

app = FastAPI()

@app.post("/predict", response_model=PredictionOutput, status_code=200)
async def predict_mean_temp(input: PredictionInput):    
    ml_models = ['lr', 'rfr']
    wind_speed = input.mean_wind_speed
    rainfall = input.daily_rainfall_total
    ml_model = input.ml_model
    prediction = 0
    
    if input.ml_model.lower() not in ml_models:
        raise ValueError("Invalid ML model input")
    
    prediction = predict.predict_temp(wind_speed, rainfall, ml_model)
 
    result = PredictionOutput(mean_wind_speed=wind_speed, daily_rainfall_total=rainfall, ml_model=ml_model, predicted_mean_temperature=prediction)
    return result