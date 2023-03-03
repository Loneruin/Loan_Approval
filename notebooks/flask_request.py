from flask import Flask, jsonify, Request
from flask_restful import Resource, Api, reqparse
import pickle


app = Flask(__name__)
api = Api(app)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

class Prediction(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        data = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()

        prediction = model.predict(data)

        return jsonify({'prediction': list(prediction)})
    
api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)