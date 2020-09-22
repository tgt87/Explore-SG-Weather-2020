# Explore-SG-Weather-2020
Exploratory Data Analysis (EDA) of 2020 Singapore weather. <br/>
4 different areas were chosen as to represent the different regions of Sinagpore to perform the analysis
* Ang Mo Kio
* Changi
* Jurong (West)
* Newton

The datasets were obtained from http://www.weather.gov.sg/climate-historical-daily/

## EDA
![Alt text](/assets/img/weather.png?raw=true "Weather line plot")
![Alt text](/assets/img/wind_rain_scatter.png?raw=true "Wind Rain Scatter Plot")
![Alt text](/assets/img/corr_matrix.png?raw=true "Correlation matrix")

## Prediction of temperature using wind speed and rainfall
Linear Regression - MSE: 0.8541, R2 score: 0.1934
<br/>
Random Forest Regressor - MSE: 0.8685, R2 score: 0.1797

## Prediction of whether it rained using temperature and wind speed
Logistic regression - Accuracy: 74%
<br/>
![Alt text](/assets/img/logreg_decision_boundary.png?raw=true "Decision boundary")
![Alt text](/assets/img/roc.png?raw=true "ROC")

## API for prediction (Build with FastAPI)
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
### To predict temperatue:
Submit a POST request to http://127.0.0.1:8000/predict/temp 

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

### To predict whether it rained:
Submit a POST request to http://127.0.0.1:8000/predict/rain

Sample request:
```
{
	"mean_temp": 29.5,
    "mean_wind_speed": 4.0
}
```

Sample response:
```
{
    "mean_temp": 29.5,
    "mean_wind_speed": 4.0,
    "predicted_rain": false
}
```