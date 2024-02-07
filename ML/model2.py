import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

df = pd.read_csv("../data/rad_food_dataset.csv")

# Convert categorical variables (gender and activity_level) into numerical values using one-hot encoding
df = pd.get_dummies(df, columns=['activity_level'], drop_first=True)
# df = pd.get_dummies(df, columns=['gender', 'activity_level'], drop_first=True)

# Drop non-numeric columns and unnecessary columns
df.drop(['gender','name', 'recommended_foods_breakfast', 'recommended_foods_lunch', 'recommended_foods_dinner'], axis=1, inplace=True)

# Feature Engineering

# Combine the independent features into a single feature vector
df['features'] = df.apply(lambda row: row[['age', 'daily_calorie_limit']].values.tolist(), axis=1)

# Model Building

# Use CountVectorizer to convert the feature vectors into a matrix of token counts
vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(df['features'].astype(str))

# Include daily_calorie_limit in the cosine similarity calculation
cosine_sim = cosine_similarity(feature_matrix, feature_matrix)

# Save the model components using joblib
joblib.dump(vectorizer, 'vectorizer.joblib')
joblib.dump(cosine_sim, 'cosine_sim.joblib')

# Get user input for daily_calorie_limit
user_daily_calorie_limit = float(input("Enter your daily calorie limit: "))

# Create a user vector for similarity comparison
user_vector = [0, 0, 0, user_daily_calorie_limit]

# Find most similar patients to the user
similarity_scores = cosine_similarity([user_vector], feature_matrix)[0]
similar_patients = list(enumerate(similarity_scores))
similar_patients = sorted(similar_patients, key=lambda x: x[1], reverse=True)[1:4]  # Get the top 3 most similar patients

# Recommend foods based on the most similar patient
recommended_foods = {
    'breakfast': [],
    'lunch': [],
    'dinner': []
}

for index, score in similar_patients:
    recommended_foods['breakfast'].extend(df.iloc[index]['recommended_foods_breakfast'])
    recommended_foods['lunch'].extend(df.iloc[index]['recommended_foods_lunch'])
    recommended_foods['dinner'].extend(df.iloc[index]['recommended_foods_dinner'])

# Display recommendations
print(f"\nRecommended Breakfast: {recommended_foods['breakfast']}")
print(f"Recommended Lunch: {recommended_foods['lunch']}")
print(f"Recommended Dinner: {recommended_foods['dinner']}")

