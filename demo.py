import pandas as pd

# Define a function to extract table information and recommend food
def recommend_food(table_df):
    # Extract relevant rows from the DataFrame
    table_info = table_df.iloc[4:]  # Assuming relevant information starts from row 5
    # Set the first row as the column headers
    table_info.columns = table_info.iloc[0]
    # Drop the first row (as it is now column headers)
    table_info = table_info[1:]
    
    # You can now access the relevant columns for recommendation
    recommended_food = table_info[['Name', 'Proteins', 'Carbls', 'Fats', 'Fiber', 'Cal']]

    # Further processing or filtering based on your criteria
    # For example, you can filter based on specific conditions:
    # recommended_food = recommended_food[(recommended_food['Proteins'] >= min_proteins) & ...]

    return recommended_food

# Load your DataFrames (replace 'table1.csv' with the actual file path)
table1 = pd.read_csv('table1.csv')
table2 = pd.read_csv('table2.csv')
# Load other tables similarly

# Call the function for each table
recommended_food_table1 = recommend_food(table1)
recommended_food_table2 = recommend_food(table2)
# Call for other tables

# You can now access the recommended foods for each table
print(recommended_food_table1)
print(recommended_food_table2)
# Print others as needed