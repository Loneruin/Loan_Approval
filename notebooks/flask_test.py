from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle
app = Flask(__name__)
api = Api(app)

# import models

with open('model_columns.pkl', 'rb') as f:
   model_columns = pickle.load (f)

with open('regressor.pkl', 'rb') as f:
    logreg = pickle.load(f)

outputs = ['It may be difficult to get approved.','We can get you approved!']
class Prediction(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()

        prediction = logreg.predict(df)

        return outputs[prediction[0]]
    
api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)