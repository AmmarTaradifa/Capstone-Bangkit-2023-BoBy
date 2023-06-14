import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np
from recommendation import recommend_items, calculate_bmr

# Load the model data
with open('model.pkl', 'rb') as f:
    model_data = pickle.load(f)
    food_names = model_data['food_names']
    calories = model_data['calories']

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation API endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input from the request
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    age = int(request.form['age'])
    gender = request.form['gender']
    activity_level = request.form['activity_level']

    # Calculate BMR and daily calorie intake
    bmr = calculate_bmr(height, weight, age, gender)
    activity_factors = {'sedentary': 1.2, 'mild': 1.375, 'normal': 1.55, 'active': 1.725, 'energetic': 1.9}
    activity_level = activity_level.lower()

    # Check for activity level variations
    if activity_level in activity_factors:
        daily_calorie_intake = bmr * activity_factors[activity_level]
    else:
        if activity_level == 's':
            daily_calorie_intake = bmr * activity_factors['sedentary']
        elif activity_level == 'm':
            daily_calorie_intake = bmr * activity_factors['mild']
        elif activity_level == 'n':
            daily_calorie_intake = bmr * activity_factors['normal']
        elif activity_level == 'a':
            daily_calorie_intake = bmr * activity_factors['active']
        elif activity_level == 'e':
            daily_calorie_intake = bmr * activity_factors['energetic']
        else:
            print("Invalid activity level")
            exit()

    # Get recommended foods
    recommended_foods = recommend_items(daily_calorie_intake, food_names, calories)

    # Prepare the response
    response = {
        'BMR': bmr,
        'Daily Calorie Intake': daily_calorie_intake,
        'Recommended Foods': recommended_foods
    }

    return jsonify({'Rekomendasi': response})


if __name__ == '__main__':
    app.run(debug=True)
