import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. SETUP: Load your data and prepare it
file_path = r'D:\Study\Programming\machine_learning\logistic_regression.csv'
df = pd.read_csv(file_path)

# Define the features (X) and the target (y)
X = df[['Studied', 'Slept']]
y = df['Passed']


# 2. THE MODEL: Create and train the model
# We train on all the data to visualize the boundary the model learns from it
model = LogisticRegression()
model.fit(X, y)


# 3. VISUALIZATION: Plot the data points and the decision boundary

# Create a scatter plot of the actual data
# c=y colors the points based on whether they passed (1) or failed (0)
plt.scatter(df['Studied'], df['Slept'], c=y, cmap='coolwarm', edgecolor='k', label='Actual Data')

# Create a grid to plot the decision boundary on
# ax = plt.gca()
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()

# # Create a meshgrid of points across the plot
# xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 100),
#                        np.linspace(ylim[0], ylim[1], 100))

# # Get the model's prediction for every point on the grid
# Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)

# # Plot the decision boundary by filling the regions with color
# # The alpha=0.3 makes the colors transparent
# plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.3)

# Add labels and a title for clarity
plt.title('Logistic Regression Decision Boundary')
plt.xlabel('Hours Studied')
plt.ylabel('Hours Slept')
plt.show()