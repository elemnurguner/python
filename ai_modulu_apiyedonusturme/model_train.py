import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump

# Örnek veri oluşturma (Sıcaklık ↔ Dondurma Satışları)
temperatures = np.array([20, 22, 24, 26, 28, 30, 32]).reshape(-1, 1)
sales = np.array([50, 60, 75, 80, 90, 100, 110])

# Modeli eğitme
model = LinearRegression()
model.fit(temperatures, sales)

# Modeli kaydetme
dump(model, 'icecream_model.joblib')
print("Model başarıyla kaydedildi!")