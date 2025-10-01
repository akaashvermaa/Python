#We will first import necessary libraries 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

file_path  = r'D:\Study\Programming\matplotlib\tips.csv'
df = pd.read_csv(file_path)

X = df[['total_bill']] # Double square brackets used for beacuse it should be a 2D Array 
y = df['tip']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"The average error of our model's predictions is: ${mae:.2f}")
print(predictions)