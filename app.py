from cgitb import text
from distutils.log import debug
from email import message
from http.client import responses
from  flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response 

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    responses = get_response(text)
    message = {"answer": responses}
    return jsonify(message)

if __name__ ==  "__main__":
    app.run(debug=True)
