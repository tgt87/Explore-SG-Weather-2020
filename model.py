from pydantic import BaseModel
from typing import Optional

class PredictTempInput(BaseModel):
    mean_wind_speed: float
    daily_rainfall_total: float
    ml_model: Optional[str] = 'lr'

class PredictTempOutput(PredictTempInput):
    predicted_mean_temperature: float

class PredictRainInput(BaseModel):
    mean_temp: float
    mean_wind_speed: float

class PredictRainOutput(PredictRainInput):
    predicted_rain: bool