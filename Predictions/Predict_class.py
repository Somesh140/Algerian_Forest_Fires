import sys
import pickle
import pandas as pd
import numpy as np
import sklearn



# adding Folder to the system path
sys.path.insert(0, 'Algerian_Forest_Fires/application_logging') # Define path based on your OS
from application_logging.app_logger import log

# adding Folder to the system path

sys.path.insert(0, 'Algerian_Forest_Fires/Data_prep_classification') # Define path based on your OS
from Data_prep_classification.prep_classification import prepdata

#loading Classification model
model=pickle.load(open('Models/model_classification_adaboost.pkl','rb'))

def fire(data):
    """ This function preprocessesthe data collected from the flask app using object of the
        prepdata class and its methods 
        --------------------------------
        Args:
        data: Dictionary"""
    try:
        PC = prepdata()
        d1 = pd.DataFrame(data)
        print(d1)
        d2 = PC.addfeature(d1)
        print(d2)
        d3 = PC.dropfeature(d2)
        print(d3)
        d4 = PC.month_weightage(d3)
        print(d4)
        d5 = PC.scaling(d4)
        print(d5)
        return d5
    except Exception as e:
        log.error("error in excecuting fire function")
        print(e)

