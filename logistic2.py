import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. SETUP: Create our fruit dataset
data = {
    'weight_g': [155, 165, 140, 205, 190, 220, 160, 215],
    'color_score': [2, 1, 3, 9, 10, 8, 2, 9]
}
# We define the "answers" or labels for our data
# 0 = Apple, 1 = Orange
target = [0, 0, 0, 1, 1, 1, 0, 1] 

# Create a DataFrame from our data
df = pd.DataFrame(data)
df['fruit'] = target


# 2. DATA PREPARATION: Define features and target, then split
# Features (the clues our model will use)
X = df[['weight_g', 'color_score']]
# Target (the answer our model needs to learn)
y = df['fruit']

# Split the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# 3. THE MODEL: Create and train the Logistic Regression model
# Create the model object
model = LogisticRegression()

# Train the model on our fruit data so it learns the patterns
model.fit(X_train, y_train)


# 4. PREDICTION: Make a guess on a new, unseen fruit
# Let's create a new fruit that weighs 195g and has a color score of 8
mystery_fruit = [[195, 8]] 

# Use the trained model to predict if it's an Apple (0) or Orange (1)
prediction = model.predict(mystery_fruit)

# Print the result in a user-friendly way
if prediction[0] == 0:
    print("The model predicts the mystery fruit is an Apple! ")
else:
    print("The model predicts the mystery fruit is an Orange! ")


# 5. EVALUATION: Check how accurate our model is
# Use the model to make predictions on the test data (the data it didn't see during training)
test_predictions = model.predict(X_test)

# Compare the model's predictions to the actual answers
accuracy = accuracy_score(y_test, test_predictions)

# Print the accuracy as a percentage
print(f"\nModel Accuracy on the test set: {accuracy * 100:.2f}%")