import pickle, os, sys
import pandas as pd
import numpy as np

folder = "ML_models"

def temp(wind_speed, rainfall, ml_model):   
    params = {"Mean Wind Speed (km/h)": [wind_speed], "Daily Rainfall Total (mm)": [rainfall]}
    mean_temp = 0
    model_filename = ml_model + '_model.pkl'
    
    try:
        with open(os.path.join(folder,model_filename), 'rb') as f:
            regression_model = pickle.load(f)
            predict = regression_model.predict(pd.DataFrame(params))
            if(ml_model == 'rfr'):
                mean_temp = round(predict[0],1)
            else:
                mean_temp = round(predict[0][0],1)
    except IOError as e:
        raise IOError("I/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        raise Exception("Unexpected error:", sys.exc_info()[0])

    return mean_temp

def rain(temp, wind_speed):
    is_rain = False
    try:
        with open(os.path.join(folder,'logr_model.pkl'), 'rb') as f:
            logreg_model = pickle.load(f)
            predict = logreg_model.predict(np.array([[temp,wind_speed]]))
            is_rain = predict[0]
    except IOError as e:
        raise IOError("I/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        raise Exception("Unexpected error:", sys.exc_info()[0])

    return is_rain