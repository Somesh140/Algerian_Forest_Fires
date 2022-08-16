import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler 
from application_logging.app_logger import log
import scipy.stats as stat

class prepdata:
    """This class will be used to preprocess the data before prediction"""
    
    def addfeature(self,data):
        """Method name: addfeature
            Description: To add feature FFMC_box which is box-cox transformation of
            FFMC value
           ------
            Args:
            ------
            data: DataFrame """
        try:
            data['FFMC_box']=stat.boxcox(data['FFMC'])[0]
            print("FFMC_box added successfully")
            log.info("FFMC_box added successfully")
            return data
        except Exception as e:
            log.error("Error occurred in adding FFMC_box")
            raise e

    def dropfeature(self,data):
        """Method name: dropfeature
            Description : It drops year,day,FFMC,BUI,FWI,columns
            ------
            Args:
            ------
            data: DataFrame"""
        try:
            data=data.drop(columns=['year','day','FWI','FFMC','BUI'])
            print("day,year,BUI,FWI,FFMC columns are dropped")
            log.info("day,year,BUI,FWI,FFMC columns are dropped")
            return data
        except Exception as e:
            log.error("Error occurred in deleting columns")
            raise e
    
    def month_weightage(self,data):
        """Method name: month_weightage
            Description: It gives weightage to months
            -----------------
            June(06):       2
            July(07):       3
            August(08):     4
            September(09):  1 
            -----
            Args:
            ------
            data: DataFrame"""
        try:
            data['month']=data['month'].map({'06':2, '07':3 , '08':4 , '09':1})
            print("weights added")
            log.info("Weights added to months")
            return data
        except Exception as e:
            log.error("error is weight assignment")
            raise e

    def scaling(self,data):
        """Methodname: scaling
            Description: It performs standardisation of the data entered
            -----
            Args:
            ------
            data: DataFrame"""
        try:
            scalar = StandardScaler()
            data_scaled = pd.DataFrame(scalar.fit_transform(data),columns=data.columns)
            print("Sacaling performed")
            log.info("Scaling performed")
            return data_scaled
        except Exception as e:
            print(e)
            log.error("Scaling cannot be preformed")
            raise e
