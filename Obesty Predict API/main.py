import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('decision_model.pkl', 'rb'))
scaler = pickle.load(open('standar.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    weight = float(request.form['weight'])
    riwayat = request.form['riwayat']
    height = float(request.form['height'])
    age = int(request.form['Age'])
    favc = request.form['FAVC']

    if riwayat == 'yes':
        riwayat = 1
    else:
        riwayat = 0

    if favc == 'yes':
        favc = 1
    else:
        favc = 0

    input_data = [weight, riwayat, height, age, favc]
    input_data_std = scaler.transform([input_data])

    prediction = model.predict(input_data_std)[0]

    if prediction == 0:
        prediction_text = 'Normal Weight'
    elif prediction == 1:
        prediction_text = 'Overweight Level I'
    elif prediction == 2:
        prediction_text = 'Overweight Level II'
    elif prediction == 3:
        prediction_text = 'Obesity Type I'
    elif prediction == 4:
        prediction_text = 'Insufficient Weight'
    elif prediction == 5:
        prediction_text = 'Obesity Type II'
    else:
        prediction_text = 'Obesity Type III'

    # return render_template('index.html', prediction_text=prediction_text)
    return jsonify({'prediction': prediction_text})


if __name__ == "__main__":
    app.run(debug=True)