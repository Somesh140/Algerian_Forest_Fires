from flask_cors import cross_origin
from flask import Flask, request,render_template,url_for
import pickle
import sklearn
from application_logging.app_logger import log
import numpy as np
import pandas as pd
from Predictions.Predict_class import fire
#creating flask app
app = Flask(__name__)

#Route for loading homepage
@app.route('/',methods=['GET','POST'])
@cross_origin()
def homepage():
    log.info("Homepage_loaded_successfully")
    print("homepage loaded successfully")
    return render_template("home.html")

#Route for homepage selection
@app.route('/prediction_choice',methods=['GET','POST'])
@cross_origin()
def prediction_choice():
    try:
        if request.method=='POST':
            choice=request.form['choice']
            if choice=='single':
                print("single prediction")
                log.info("choice is single prediction")
                return render_template("single_prediction.html",title='Single Prediction')
            else:
                print("bulk prediction")
                log.info("choice is bulk prediction")
                return render_template("bulk_prediction.html",title='Bulk prediction')
        log.info("Rendering prediction choice page")
    except Exception as e:
        print(e)
        log.error("error while rending prediction page")

#Route to show single predictionin web UI
@app.route('/single_prediction',methods=['GET','POST'])
@cross_origin()
def single_prediction():
    if request.method=='POST':
        try:
            day=int(request.form['day'])
            month=request.form['month']
            year=int(request.form['year'])
            RH=float(request.form['RH'])
            Ws = float(request.form['Ws'])
            Rain = float(request.form['Rain'])
            FFMC = float(request.form['FFMC'])
            DMC = float(request.form['DMC'])
            DC = float(request.form['DC'])
            ISI = float(request.form['ISI'])
            BUI = float(request.form['BUI'])
            FWI = float(request.form['FWI'])
            Temp=float(request.form['Temp'])
            print(day,month,year,Temp,RH,Ws,Rain,FFMC,DMC,DC,ISI,BUI,FWI)
            log.info("Data Entered")
            return "Everything is right"
        except Exception as e:
            log.error("Something went wrong")
            print(e)
            return "something is wrong"
    else:
        render_template("home.html")

# Predicting classification through postman
@app.route('/predict_postman',methods = ['POST'])
@cross_origin()
def predict_via_postman():#for calling the API from Postman
    try:
        data = request.json['data']
        print("data is ",data)
        #lg.info("data entered : ",data)
        new_data = [list(data.values())]
        print("new_data is ",new_data)

        # predicting output
        output = model.predict(new_data)[0]
        print(output)
        #lg.info("model predicted: ",output)

        return jsonify(output)

    except Exception as e:
        #lg.error("Error: ",e)
        print(e)
        return "wrong input"


if __name__ =="__main__":
    app.run(debug=True)