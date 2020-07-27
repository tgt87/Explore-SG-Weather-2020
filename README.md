# Explore-SG-Weather-2020
Exploratory Data Analysis (EDA) of Singapore weather in the first half of 2020. <br/>
4 different areas were chosen as to represent the different regions of Sinagpore to perform the analysis
* Ang Mo Kio
* Changi
* Jurong (West)
* Newton

The datasets were obtained from http://www.weather.gov.sg/climate-historical-daily/

## EDA
![Alt text](/assets/img/weather_eda_result.png?raw=true "Weather EDA result")
![Alt text](/assets/img/wind_rain_scatter.png?raw=true "Wind Rain Scatter Plot")
![Alt text](/assets/img/corr_matrix.png?raw=true "Correlation matrix")

## Prediction of mean temperature using mean wind speed and daily rainfall total
Linear Regression - MSE: 0.7202, R2 score: 0.0847
<br/>
Random Forest Regressor - MSE: 0.7727, R2 score: 0.0180

## API for mean temperature prediction (Build with FastAPI)
### Requirements
Python 3.6+

### Installation
```
$ pip install -r requirements.txt
```
### Run
```
$ uvicorn api:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
Submit a POST request to http://127.0.0.1:8000/predict 

Sample request:
```
{
    "mean_wind_speed": 6.0,
    "daily_rainfall_total": 30.4,
    "ml_model": "lr"
}
```
Note: ml_model accepts either "lr" or "rfr" and is optional, default value is "lr".

Sample response:
```
{
    "mean_wind_speed": 6.0,
    "daily_rainfall_total": 30.4,
    "ml_model": "lr",
    "predicted_mean_temperature": 27.4
}
```