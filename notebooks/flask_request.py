from flask import Flask, jsonify, Request
from flask_restful import Resource, Api, reqparse
import pickle


app = Flask(__name__)
api = Api(app)

# import models

with open('model_columns.pkl', 'rb') as f:
   model_columns = pickle.load (f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
# web page
@app.route('/')
def welcome():
   return "Welcome! Use this Flask App for Loan Approval Prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return "Prediction page. Try using post with params to get specific prediction."

   if flask.request.method == 'POST':
       try:
           json_ = request.json # '_' since 'json' is a special word
           print(json_)
           query_ = pd.get_dummies(pd.DataFrame(json_))
           query = query_.reindex(columns = model_columns, fill_value= 0)
           prediction = list(model.predict(query))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })



if __name__ == "__main__":
   app.run()
