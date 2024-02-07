import pickle 
import random

with open('data/food_Info.pkl', 'rb') as f:
    food_tables = pickle.load(f)
    

def recommend_food(calorie_limit):
    food_names = []
    selected_foods_breakfast = []
    selected_foods_lunch = []
    selected_foods_dinner = []

    remaining_calories_breakfast = int(calorie_limit * 0.4)
    remaining_calories_lunch = int(calorie_limit * 0.3)
    remaining_calories_dinner = int(calorie_limit * 0.3)

    i = 0
    while remaining_calories_breakfast > 0:
        # Choose a random food table
        if i < 2:
            table_name = list(food_tables.keys())[14]
            table = food_tables[table_name]
            if list(table.values())[0][0][5] == 1:
                # Choose a random food item from the selected table
                food_name = random.choice(list(table.keys()))  
                food_calories = table[food_name][0][4]
                selected_foods_breakfast.append((food_name, food_calories))
                remaining_calories_breakfast -= food_calories
            i+=1
        else:
            table_name = random.choice(list(food_tables.keys()))
            
            table = food_tables[table_name]
            
            if list(table.values())[0][0][5] == 1:
                # Choose a random food item from the selected table
                food_name = random.choice(list(table.keys()))
                
                food_calories = table[food_name][0][4]

                # Check if adding the food exceeds the remaining calories
                # if abs(remaining_calories_breakfast - food_calories) in range(50):
                if food_name not in food_names:
                    selected_foods_breakfast.append((food_name, food_calories))
                    remaining_calories_breakfast -= food_calories
                    food_names.append(food_name)
                    print("ADD food ", food_name)
                    
                else:
                    print("not food ", food_name)
    
    i = 0       
    while remaining_calories_lunch > 0:
        # Choose a random food table
        if i < 1:
            table_name = list(food_tables.keys())[0]
            
            table = food_tables[table_name]
            if list(table.values())[0][0][6] == 1:
                # Choose a random food item from the selected table
                food_name = random.choice(list(table.keys()))
                
                if food_name != "Plain Steamed Rice (1 Small Bowl)":
                    food_calories = table[food_name][0][4]
                    selected_foods_lunch.append((food_name, food_calories))
                    remaining_calories_lunch -= food_calories
                
            i+=1
            # print(table , food_name,"  jhsbhjesd")

        else:
            table_name = random.choice(list(food_tables.keys()))
            table = food_tables[table_name]
            
            if list(table.values())[0][0][6] == 1:
                # Choose a random food item from the selected table
                food_name = random.choice(list(table.keys()))
                
                if food_name != "Plain Steamed Rice (1 Small Bowl)":
                    food_calories = table[food_name][0][4]

                    # Check if adding the food exceeds the remaining calories
                    # if abs(remaining_calories_breakfast - food_calories) in range(50):
                    if food_name not in food_names:
                        selected_foods_lunch.append((food_name, food_calories))
                        remaining_calories_lunch -= food_calories
                        food_names.append(food_name)
                    
        
    i = 0      
    while remaining_calories_dinner > 0:
        if i < 1:
            table_name = list(food_tables.keys())[0]
            
            table = food_tables[table_name]
            if list(table.values())[0][0][6] == 1:
                # Choose a random food item from the selected table
                food_name = random.choice(list(table.keys()))
                
                if food_name != "Plain Steamed Rice (1 Small Bowl)":
                    food_calories = table[food_name][0][4]
                    selected_foods_dinner.append((food_name, food_calories))
                    remaining_calories_dinner -= food_calories
                
            i+=1
            # print(table , food_name,"  jhsbhjesd")
            
        else:
            table_name = random.choice(list(food_tables.keys()))
            table = food_tables[table_name]
            # Choose a random food table
            table_name = random.choice(list(food_tables.keys()))
            table = food_tables[table_name]
            
            if list(table.values())[0][0][7] == 1:
                # Choose a random food item from the selected table
                food_name = random.choice(list(table.keys()))
                
                if food_name != "Plain Steamed Rice (1 Small Bowl)":
                    food_calories = table[food_name][0][4]

                    # Check if adding the food exceeds the remaining calories
                    # if abs(remaining_calories_breakfast - food_calories) in range(50):
                    if food_name not in food_names:
                        selected_foods_dinner.append((food_name, food_calories))
                        remaining_calories_dinner -= food_calories
                        food_names.append(food_name)
                    

    return selected_foods_breakfast, selected_foods_lunch, selected_foods_dinner

if __name__ == '__main__':

    daily_calorie_limit = 1500
    recommended_foods_breakfast, recommended_foods_lunch, recommended_foods_dinner = recommend_food(daily_calorie_limit)

    t_b = 0
    print("Recommended foods for Breakfast:")
    for food, calories in recommended_foods_breakfast:
        t_b += calories
        print(f"{food}: {calories} calories")
    print("-"*50 , f"Total Breakfast Recommended {t_b} calories" , "-"*50)
    print()

    t_l = 0
    print("\nRecommended foods for Lunch:")
    for food, calories in recommended_foods_lunch:
        t_l += calories
        print(f"{food}: {calories} calories")
    print("-"*50 , f"Total Lunch Recommended {t_l} calories" , "-"*50)

    print()

    t_d = 0
    print("\nRecommended foods for Dinner:")
    for food, calories in recommended_foods_dinner:
        t_d += calories
        print(f"{food}: {calories} calories")
    print("-"*50 , f"Total Dinner Recommended {t_d} calories" , "-"*50)


    print("*"*50 , f"Total Recommended {t_d + t_b + t_l} calories" , "*"*50)

