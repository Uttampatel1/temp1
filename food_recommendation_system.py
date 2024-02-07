import random

class FoodRecommendationSystem:
    def __init__(self):
        self.recommended_foods = []

    def recommend_food(self, health_conditions, bmi=None, bmr=None, calorie_intake=None):
        recommended_breakfast = []
        recommended_lunch = []
        recommended_dinner = []

        # Rule-based recommendations based on health conditions, BMI, and BMR
        if "cardiac" in health_conditions:
            # Recommendations for Breakfast
            recommended_breakfast.extend(self.limit_saturated_and_trans_fats())
            recommended_breakfast.extend(self.emphasize_whole_grains())
            recommended_breakfast.extend(self.encourage_fruits_and_vegetables())
            recommended_breakfast.extend(self.control_sodium_intake())
            recommended_breakfast.extend(self.monitor_cholesterol())
            recommended_breakfast.extend(self.control_portion_sizes())

            # Recommendations for Lunch
            recommended_lunch.extend(self.limit_saturated_and_trans_fats())
            recommended_lunch.extend(self.emphasize_whole_grains())
            recommended_lunch.extend(self.encourage_fruits_and_vegetables())
            recommended_lunch.extend(self.control_sodium_intake())
            recommended_lunch.extend(self.monitor_cholesterol())
            recommended_lunch.extend(self.control_portion_sizes())

            # Recommendations for Dinner
            recommended_dinner.extend(self.limit_saturated_and_trans_fats())
            recommended_dinner.extend(self.emphasize_whole_grains())
            recommended_dinner.extend(self.encourage_fruits_and_vegetables())
            recommended_dinner.extend(self.control_sodium_intake())
            recommended_dinner.extend(self.monitor_cholesterol())
            recommended_dinner.extend(self.control_portion_sizes())

        # Additional recommendations based on BMI and BMR
        if bmi:
            if bmi < 18.5:
                # Recommendations for Breakfast
                recommended_breakfast.extend(self.high_calorie_foods())
            elif 18.5 <= bmi <= 24.9:
                # Recommendations for Breakfast
                recommended_breakfast.extend(self.balanced_diet_foods())

        if bmr:
            if bmr < 1500:
                # Recommendations for Lunch
                recommended_lunch.extend(self.low_calorie_foods())
            elif 1500 <= bmr <= 2000:
                # Recommendations for Lunch
                recommended_lunch.extend(self.moderate_calorie_foods())
            elif bmr > 2000:
                # Recommendations for Lunch
                recommended_lunch.extend(self.high_calorie_foods())

        # Additional recommendations based on calorie intake
        if calorie_intake:
            if calorie_intake < 1500:
                # Recommendations for Dinner
                recommended_dinner.extend(self.low_calorie_foods())
            elif 1500 <= calorie_intake <= 2000:
                # Recommendations for Dinner
                recommended_dinner.extend(self.moderate_calorie_foods())
            elif calorie_intake > 2000:
                # Recommendations for Dinner
                recommended_dinner.extend(self.high_calorie_foods())
                
                # random.sample(self.recommended_foods, min(3, len(self.recommended_foods)))
                
        recommended_breakfast = random.sample(recommended_breakfast , min(3, len(recommended_breakfast)))
        recommended_lunch = random.sample(recommended_lunch , min(6, len(recommended_lunch)))
        recommended_dinner = random.sample(recommended_dinner , min(7, len(recommended_dinner)))

        return recommended_breakfast , recommended_lunch, recommended_dinner

    def balanced_diet_foods(self):
        # Example: Balanced diet foods
        return [
            {"food": "Balanced Food1", "calories": 120},
            {"food": "Balanced Food2", "calories": 150},
            {"food": "Balanced Food3", "calories": 180},
        ]


    def limit_saturated_and_trans_fats(self):
        return [
            {"food": "Avocados", "calories": 160},
            {"food": "Nuts", "calories": 200},
            {"food": "Seeds", "calories": 180},
            {"food": "Olive oil", "calories": 120},
            {"food": "Fatty fish", "calories": 250},
            {"food": "Lean proteins", "calories": 180},
        ]

    def emphasize_whole_grains(self):
        return [
            {"food": "Whole grains", "calories": 150},
            {"food": "High-fiber foods", "calories": 120},
        ]

    def encourage_fruits_and_vegetables(self):
        return [
            {"food": "Colorful fruits and vegetables", "calories": 100},
            {"food": "At least 5 servings a day", "calories": 80},
        ]

    def control_sodium_intake(self):
        return [
            {"food": "Fresh fruits and vegetables", "calories": 100},
            {"food": "Herbs and spices", "calories": 10},
            {"food": "Low-sodium or no added salt foods", "calories": 120},
        ]

    def monitor_cholesterol(self):
        return [
            {"food": "Foods rich in soluble fiber", "calories": 140},
            {"food": "Omega-3 rich foods", "calories": 180},
        ]

    def control_portion_sizes(self):
        return [
            {"food": "Moderate portions", "calories": 90},
            {"food": "Maintain a healthy weight", "calories": 0},
        ]

    def low_calorie_foods(self):
        return [
            {"food": "Gujarati Dal", "calories": 100},
            {"food": "Bhindi Sambhariya", "calories": 120},
            {"food": "Tindora Nu Shaak", "calories": 80},
            {"food": "Palak Thepla", "calories": 90},
            {"food": "Khandvi", "calories": 110},
        ]

    def moderate_calorie_foods(self):
        return [
            {"food": "Baingan Bharta", "calories": 150},
            {"food": "Karela Nu Shaak", "calories": 130},
            {"food": "Cabbage Sabzi", "calories": 120},
            {"food": "Handvo", "calories": 160},
            {"food": "Dhokli Nu Shaak", "calories": 140},
        ]

    def high_calorie_foods(self):
        return [
            {"food": "Aloo Gobi", "calories": 200},
            {"food": "Undhiyu", "calories": 250},
            {"food": "Dhokla", "calories": 180},
            {"food": "Muthiya", "calories": 160},
            {"food": "Gujarati Kadhi", "calories": 190},
        ]
        