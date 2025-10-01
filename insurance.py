import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Load the correct dataset
file_path = r'D:\Study\Programming\machine_learning\insurance.csv'
df = pd.read_csv(file_path)

# 2. Convert text columns to numbers using one-hot encoding
df_encoded = pd.get_dummies(df, drop_first=True)


# 3. Define the Features (X) and the Target (y)
# The target is 'charges'
y = df_encoded['charges']
# The features are all columns EXCEPT 'charges'
X = df_encoded.drop('charges', axis=1)


# 4. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 5. Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)


# 6. Make predictions and evaluate the model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print(f"The model was trained on the insurance dataset.")
print(f"On average, the model's predictions for medical charges are off by: ${mae:.2f}")