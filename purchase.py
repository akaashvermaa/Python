import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
from sklearn.metrics import confusion_matrix

file_path = r'D:\Study\Programming\machine_learning\Social_Network_Ads.csv'
df = pd.read_csv(file_path)
print(df.columns)
# df.info
# print(df.info)

df.drop(['Gender', 'User ID'], axis= 1, inplace=True)

X = df[['Age','EstimatedSalary']]
y = df['Purchased']

X_train, X_test, y_train, y_test =train_test_split(X, y, test_size= 0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test,predictions)
print(f"Prediction of X_test is {accuracy*100:.2f}%")
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
# sns.lineplot(data = df , x = 'Age', y = 'Purchased')
# plt.title("Predicting Car Purchase")
# plt.show()