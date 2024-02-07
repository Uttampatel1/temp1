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
