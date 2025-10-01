import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

file_path = r'D:\Study\Programming\matplotlib\tips.csv'
df =pd.read_csv(file_path)

# (Your code for creating X and y)
...
X = df[['total_bill']]
y = df['tip']

# --- DEBUGGING STEP: Add this line ---
print("Shape of the data before splitting:", X.shape) 

# If the output of the line above is (1, ...), you have found the problem.

# Now, split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train , y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
print(f"The average error of our model's predictions is: ${mae:.2f}")

plt.scatter(X_test, y_test , color = 'grey', label = 'Actual Data')
plt.plot(X_test, predictions, color='red', linewidth=2, label='Model Prediction Line')
plt.title('Model Prediction vs Actual Data')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.legend()
plt.show()



'''
We start by importing all the tools we need: pandas to handle our data, train_test_split to divide our data, LinearRegression for our model, mean_absolute_error to score our model, and matplotlib.pyplot to visualize the results.

2. Data Preparation
Load Data: We load tips.csv into a DataFrame called df.

Define Features & Target: We tell our model what to learn from and what to predict.

X = df[['total_bill']]: The Feature is our "clue." It's the information we give the model. We use double brackets [[]] to make it a 2D DataFrame.

y = df['tip']: The Target is our "answer." It's what we want the model to learn to predict.

Split Data: We use train_test_split to divide our data. The model will train on the _train sets and will be evaluated on the unseen _test sets. This prevents the model from cheating by testing it on data it has never seen before

The Model
Create Model: model = LinearRegression() creates a fresh, empty Linear Regression model.

Train Model: model.fit(X_train, y_train) is the most important step. The model looks at all the total_bill values and their corresponding tip values in the training data and calculates the single best-fitting straight line to describe that relationship. This is the learning phase.

4. Results & Evaluation
Make Predictions: predictions = model.predict(X_test) uses the line the model learned to guess the tip for each total_bill in the unseen test set.

Evaluate Performance: mean_absolute_error(...) compares the model's predictions to the y_test (the actual answers). The result tells us, on average, how many dollars and cents our model's guess was off by.

Visualize: The plt.scatter() and plt.plot() commands draw a picture of our results, showing the actual data points and the prediction line our model learned. This gives us a quick visual confirmation of how well the model performed.
'''