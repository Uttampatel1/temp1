# import pickle
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score

# # Load your dataset (replace 'your_dataset.pkl' with your actual dataset)
# with open('/workspaces/codespaces-blank/data/your_dataset.pkl', 'rb') as f:
#     dataset = pickle.load(f)

# # Assuming your dataset has features and labels
# features = dataset['features']
# labels = dataset['labels']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# # Build a decision tree classifier (replace this with a more suitable model)
# model = DecisionTreeClassifier()

# # Train the model
# model.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = model.predict(X_test)

# # Evaluate the model accuracy (replace this with appropriate evaluation for your use case)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Model Accuracy: {accuracy}')

# # Now, you can use the trained model to recommend food
# def recommend_food_ml(model, features):
#     recommended_foods = []

#     for feature in features:
#         # Make predictions using the trained model
#         prediction = model.predict([feature])[0]

#         if prediction == 'Breakfast':
#             recommended_foods.append(('Breakfast Food', 200))  # Replace with actual food and calories
#         elif prediction == 'Lunch':
#             recommended_foods.append(('Lunch Food', 300))  # Replace with actual food and calories
#         elif prediction == 'Dinner':
#             recommended_foods.append(('Dinner Food', 400))  # Replace with actual food and calories

#     return recommended_foods

# # Example usage of the recommendation function
# features_to_predict = [[...]]  # Replace with the actual features you want to predict
# recommended_foods_ml = recommend_food_ml(model, features_to_predict)

# # Print the recommended foods
# print("Recommended foods using ML:")
# for food, calories in recommended_foods_ml:
#     print(f"{food}: {calories} calories")

import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split as surprise_train_test_split
from surprise.accuracy import accuracy_score as surprise_accuracy_score

# Load your dataset (replace 'your_dataset.pkl' with your actual dataset)
with open('/workspaces/codespaces-blank/data/your_dataset.pkl', 'rb') as f:
    dataset = pickle.load(f)

# Assuming your dataset has features and labels
features = dataset['features']
labels = dataset['labels']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Build a decision tree classifier (replace this with a more suitable model)
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model accuracy (replace this with appropriate evaluation for your use case)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')

# Collaborative filtering with Surprise library
reader = Reader(rating_scale=(0, 1))
surprise_dataset = Dataset.load_from_df(dataset[['user_id', 'item_id', 'label']], reader)
trainset, testset = surprise_train_test_split(surprise_dataset, test_size=0.2, random_state=42)

# Build a collaborative filtering model (SVD)
collab_model = SVD()
collab_model.fit(trainset)

# Make predictions on the test set
collab_predictions = collab_model.test(testset)

# Evaluate the collaborative filtering model
collab_accuracy = surprise_accuracy_score(collab_predictions)
print(f'Collaborative Filtering Accuracy: {collab_accuracy}')

# Now, you can use the trained collaborative filtering model to recommend food
def recommend_food_collab(model, user_id, item_ids):
    recommended_foods = []

    for item_id in item_ids:
        # Make predictions using the collaborative filtering model
        prediction = model.predict(user_id, item_id).est

        # Assuming a binary label (0 or 1)
        if prediction > 0.5:
            recommended_foods.append(('Recommended Food', 500))  # Replace with actual food and calories

    return recommended_foods

# Example usage of the collaborative filtering recommendation function
user_id_to_predict = 'user123'  # Replace with the actual user ID you want to predict for
item_ids_to_predict = [123, 456, 789]  # Replace with the actual item IDs you want to predict for
recommended_foods_collab = recommend_food_collab(collab_model, user_id_to_predict, item_ids_to_predict)

# Print the recommended foods from collaborative filtering
print("Recommended foods using Collaborative Filtering:")
for food, calories in recommended_foods_collab:
    print(f"{food}: {calories} calories")
