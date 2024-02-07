from flask import Flask, render_template, request
from food_recommendation_system import FoodRecommendationSystem
from food_rand import recommend_food

app = Flask(__name__)
recommendation_system = FoodRecommendationSystem()

def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

def calculate_bmr(age, weight, height, gender, activity_level):
    if gender.lower() == 'male':
        bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.75 * age)
    elif gender.lower() == 'female':
        bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        raise ValueError("Invalid gender")

    # Adjust BMR based on activity level
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'extra_active': 1.9
    }

    if activity_level.lower() in activity_multipliers:
        bmr *= activity_multipliers[activity_level.lower()]
    else:
        raise ValueError("Invalid activity level")

    return round(bmr, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = int(request.form['age'])
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        activity_level = request.form['activity_level']
        gender = request.form['gender']

        bmi = calculate_bmi(weight, height)
        bmr = calculate_bmr(age, weight, height, gender , activity_level)

        # health_conditions = ["cardiac"]
        # calorie_intake = request.form.get('calorie_intake')

        recommended_breakfast, recommended_lunch, recommended_dinner = recommend_food(bmr)
        
        
        t_b = sum([calories for food, calories in recommended_breakfast])
        t_l = sum([calories for food, calories in recommended_lunch])
        t_d = sum([calories for food, calories in recommended_dinner])
      


        print("*"*50 , f"Total Recommended {t_d + t_b + t_l} calories" , "*"*50)

        return render_template('index.html', 
                               recommended_breakfast=recommended_breakfast, 
                               recommended_lunch=recommended_lunch, 
                               recommended_dinner=recommended_dinner,
                               bmi=bmi, bmr=bmr, t_b = t_b , t_l = t_l , t_d= t_d)

    return render_template('index.html', 
                           recommended_breakfast=None, 
                           recommended_lunch=None, 
                           recommended_dinner=None,
                           bmi=None, bmr=None)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request
# from food_recommendation_system import FoodRecommendationSystem

# app = Flask(__name__)
# recommendation_system = FoodRecommendationSystem()

# def calculate_bmi(weight, height):
#     height_in_meters = height / 100
#     bmi = weight / (height_in_meters ** 2)
#     return round(bmi, 2)

# def calculate_bmr(age, weight, height, gender, activity_level):
#     if gender.lower() == 'male':
#         bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.75 * age)
#     elif gender.lower() == 'female':
#         bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
#     else:
#         raise ValueError("Invalid gender")

#     # Adjust BMR based on activity level
#     activity_multipliers = {
#         'sedentary': 1.2,
#         'light': 1.375,
#         'moderate': 1.55,
#         'active': 1.725,
#         'extra_active': 1.9
#     }

#     if activity_level.lower() in activity_multipliers:
#         bmr *= activity_multipliers[activity_level.lower()]
#     else:
#         raise ValueError("Invalid activity level")

#     return round(bmr, 2)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         age = int(request.form['age'])
#         height = int(request.form['height'])
#         weight = int(request.form['weight'])
#         activity_level = request.form['activity_level']
#         gender = request.form['gender']

#         bmi = calculate_bmi(weight, height)
#         bmr = calculate_bmr(age, weight, height, gender , activity_level)

#         health_conditions = ["cardiac"]
#         calorie_intake = request.form.get('calorie_intake')

#         recommended_foods = recommendation_system.recommend_food(health_conditions, bmi, bmr, calorie_intake)

#         return render_template('index.html', recommended_foods=recommended_foods, bmi=bmi, bmr=bmr)

#     return render_template('index.html', recommended_foods=None, bmi=None, bmr=None)

# if __name__ == '__main__':
#     app.run(debug=True)
