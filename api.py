from fastapi import FastAPI
from model import PredictTempInput, PredictTempOutput, PredictRainInput, PredictRainOutput
import predict

app = FastAPI()

@app.post("/predict/temp", response_model=PredictTempOutput, status_code=200)
async def predict_mean_temp(input: PredictTempInput):    
    ml_models = ['lr', 'rfr']
    wind_speed = input.mean_wind_speed
    rainfall = input.daily_rainfall_total
    ml_model = input.ml_model
    prediction = 0
    
    if input.ml_model.lower() not in ml_models:
        raise ValueError("Invalid ML model input")
    
    prediction = predict.temp(wind_speed, rainfall, ml_model)
 
    result = PredictTempOutput(mean_wind_speed=wind_speed, daily_rainfall_total=rainfall, ml_model=ml_model, predicted_mean_temperature=prediction)
    return result

@app.post("/predict/rain", response_model=PredictRainOutput, status_code=200)
async def predict_rain(input: PredictRainInput):    
    temp = input.mean_temp
    wind_speed = input.mean_wind_speed
    prediction = False
    
    prediction = predict.rain(temp, wind_speed)
 
    result = PredictRainOutput(mean_temp=temp, mean_wind_speed=wind_speed, predicted_rain=prediction)
    return result    