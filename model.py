from pydantic import BaseModel
from typing import Optional

class PredictionInput(BaseModel):
    mean_wind_speed: float
    daily_rainfall_total: float
    ml_model: Optional[str] = 'lr'

class PredictionOutput(PredictionInput):
    predicted_mean_temperature: float