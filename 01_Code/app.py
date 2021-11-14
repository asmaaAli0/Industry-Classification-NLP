import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input_features = [str(x) for x in request.form.values()]
    prediction = model.predict(input_features)

    return render_template('index.html', prediction_text='industry is {}'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([list(data.values())])

    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)