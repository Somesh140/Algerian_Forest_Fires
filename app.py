import logging as lg

from flask import Flask, request,jsonify
import pickle

import sklearn

#creating flask app
app = Flask(__name__)
#loading model
model=pickle.load(open('model_RF.pkl','rb'))

#creating log file
lg.basicConfig(filename="run.log",
               level=lg.DEBUG,
               format="%(asctime)s %(levelname)s %(message)s")

@app.route('/predict',methods = ['POST'])
def predict_via_postman():#for calling the API from Postman
    try:
        data = request.json['data']
        lg.info("data entered : ",data)
        new_data = [list(data.values())]

        # predicting output
        output = model.predict(new_data)[0]
        lg.info("model predicted: ",output)

        return jsonify(output)

    except Exception as e:
        lg.error("Error: ",e)
        return "wrong input"


if __name__ =="__main__":
    app.run(debug=True)