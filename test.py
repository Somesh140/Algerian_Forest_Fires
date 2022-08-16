from Predictions.Predict_class import fire


data1 =  {'day':7,
    'month':'06',
    'year':2012,
    'Temp':33,
    'RH': 54 ,
    'Ws':13,
    'Rain':0,
    'FFMC':88.2,
    'DMC':9.9,
    'DC':30.5,
    'ISI':6.4,
    'BUI':10.9,
    'FWI':7.2 }
    
new_data = fire(data1)
print("new data is {} ".format(new_data))