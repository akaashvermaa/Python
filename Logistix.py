# Classification is all about predicting a category or a label
'''
example 
is this email spam or not ?
does this image contain cat,dog or bird ?

-------------------------------------Algorithm - Logistic Regression---------------------
Important: Despite having "regression" in its name, it is a classification algorithm. It works by predicting the probability that a given input belongs to a specific category
'''
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data = iris.data , columns = iris.feature_names)
df['species'] = iris.target

print(df.head())