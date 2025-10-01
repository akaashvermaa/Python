# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error

# file_path = r'D:\Study\Programming\machine_learning\titanic.csv'
# df = pd.read_csv(file_path)

# df_encoded = pd.get_dummies(df, drop_first=True)

# X = df_encoded[['Sex']]
# y = df['Survived']

# model = LogisticRegression()
# model.fit(X,y)
# plt.scatter(df['Sex'], df['Name'], ['Cabin'], ['Fare'], edgecolor = 'black')

# plt.title("Survived Vs People")
# plt.xlabel("People ")
# plt.ylabel("Survival Rate")
# plt.show()

# This code has many errors and we will fix it by each step


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# We imported all the necessary librabires

file_path = r'machine_learning\titanic.csv'
df = pd.read_csv(file_path)
df.info
print(df.info)




# --- DATA CLEANING AND PREPARATION ---

# 1. Fill missing Age values with the median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# 2. Drop columns that are not useful for prediction
# 'PassengerId', 'Name', 'Ticket', and 'Cabin' are dropped.
# 'Embarked' is also dropped for simplicity in this example.
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)

# 3. Convert the 'Sex' column to numbers using one-hot encoding
df_encoded = pd.get_dummies(df, columns=['Sex'], drop_first=True)


# --- MODEL BUILDING ---

# 4. Correctly define Features (X) and Target (y)
# X contains all columns EXCEPT 'Survived'
X = df_encoded.drop('Survived', axis=1)
# y is ONLY the 'Survived' column
y = df_encoded['Survived']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LogisticRegression(max_iter=200) # Added max_iter to help the model converge
model.fit(X_train, y_train)

# Make predictions and evaluate the model's performance
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


# --- VISUALIZATION ---

# 5. Create a meaningful plot to see the results
# For example, let's visualize the relationship between Age and Fare, colored by survival status
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', style='Survived', s=80)

plt.title("Survival based on Age and Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.legend(title='Survived', labels=['Did not Survive', 'Survived'])
plt.show()