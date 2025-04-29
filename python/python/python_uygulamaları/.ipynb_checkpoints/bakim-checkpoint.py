import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Veri yükleme
data = pd.read_csv("sensor_data.csv")

# Eksik verileri temizleme
data = data.dropna()

# Özellikler ve hedef değişken
X = data.drop("failure", axis=1)  # Sensör verileri
y = data["failure"]  # Arıza durumu (1: Arıza, 0: Normal)

# Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Veri normalizasyonu
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)