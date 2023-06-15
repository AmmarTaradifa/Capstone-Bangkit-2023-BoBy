import numpy as np
import random

def recommend_items(daily_calorie_intake, food_names, calories):
    # Calculate the differences between the calories and the daily calorie intake
    differences = np.abs(calories - daily_calorie_intake)

    # Sort the food names based on the differences in ascending order
    sorted_indices = np.argsort(differences)
    sorted_food_names = food_names[sorted_indices]
    sorted_calories = calories[sorted_indices]

    # Calculate the total calories in the dataset
    total_calories = np.sum(calories)

    # Determine the number of recommendations based on the total calories and daily calorie intake
    min_recommendations = 5
    max_recommendations = 10
    num_recommendations = min(
        max_recommendations,
        max(min_recommendations, int(daily_calorie_intake / (total_calories / len(food_names))))
    )

    # Randomly select a subset of unique recommendations
    recommended_indices = random.sample(range(len(sorted_food_names)), num_recommendations)
    recommended_foods = [
        (sorted_food_names[i], sorted_calories[i]) for i in recommended_indices
    ]

    return recommended_foods


def calculate_bmr(height, weight, age, gender):
    if gender.lower() == 'male':
        bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
    elif gender.lower() == 'female':
        bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        raise ValueError("Invalid gender specified. Please specify 'male' or 'female'.")
    return bmr
