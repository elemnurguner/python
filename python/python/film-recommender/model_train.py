# model_train.py
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

X = np.array([[1, 0], [0, 1], [1, 1]])
y = np.array(["Matrix", "Inception", "Interstellar"])

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
