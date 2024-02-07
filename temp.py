import random
from faker import Faker

fake = Faker()

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

# Example of calculating a random BMR using faker for gender and activity level
random_age = fake.random_int(min=18, max=60)
random_weight = fake.random_uniform(50, 100)  # Assuming weight in kg
random_height = fake.random_uniform(150, 190)  # Assuming height in cm
random_gender = fake.random_element(elements=['male', 'female'])
random_activity_level = fake.random_element(elements=list(activity_multipliers.keys()))

random_bmr = calculate_bmr(random_age, random_weight, random_height, random_gender, random_activity_level)

# Print the random BMR
print(f"Random BMR: {random_bmr}")
