import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Example data (no CSV needed)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("regmodel.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ regmodel.pkl created successfully!")
