from faker import Faker
import json
import pandas as pd
from food_rand import recommend_food
from utiles import calculate_bmr

fake = Faker()

# Generate synthetic face dataset with random daily calorie limits
face_dataset = []

for _ in range(100):  # Generate data for 100 individuals
    daily_calorie_limit = fake.random_int(min=1200, max=2500)
    recommended_foods_breakfast, recommended_foods_lunch, recommended_foods_dinner = recommend_food(daily_calorie_limit)
    age = fake.random_int(min=18, max=99)
    weight = fake.random_int(min=35, max=120)
    gender = fake.random_element(elements=('Male', 'Female'))
    if gender == "Male":
        height = fake.random_int(min=160, max=185)
    else:
        height = fake.random_int(min=150, max=170)
    activity_multipliers = ['sedentary', 'light', 'moderate', 'active', 'extra_active']
    random_activity_level = fake.random_element(elements=activity_multipliers)
            
    random_bmr = calculate_bmr(age, weight, height, gender, random_activity_level)

    individual_data = {
        'name': fake.name(),
        'age': age,
        'gender': gender,
        'weight' : weight,
        'height':height,
        'activity_level':random_activity_level,
        'daily_calorie_limit': random_bmr,
        'recommended_foods_breakfast': json.dumps(recommended_foods_breakfast),
        'recommended_foods_lunch': json.dumps(recommended_foods_lunch),
        'recommended_foods_dinner': json.dumps(recommended_foods_dinner),
    }
    face_dataset.append(individual_data)

# Convert to DataFrame
df = pd.DataFrame(face_dataset)

# Save DataFrame to CSV
df.to_csv('data/temp_food_dataset.csv', index=False)
