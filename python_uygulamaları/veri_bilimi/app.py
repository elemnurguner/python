from flask import Flask, request, jsonify
import torch
import numpy as np
import os
import logging

# GRUModel sınıfını tanımla
class GRUModel(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1, dropout=0.1):
        super(GRUModel, self).__init__()
        self.gru = torch.nn.GRU(input_size, hidden_size, num_layers=num_layers, batch_first=True, dropout=dropout)
        self.fc = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h_gru, _ = self.gru(x)
        out = self.fc(h_gru[:, -1, :])
        return torch.sigmoid(out)

# Flask uygulaması başlat
app = Flask(__name__)

# Modeli yükle
model_gru = GRUModel(input_size=3, hidden_size=50, output_size=1, num_layers=2)
model_path = r"C:\Users\USER\Desktop\python_uygulamaları\veri_bilimi\gru_model.pth"

# Model dosyasının varlığını kontrol et
if os.path.exists(model_path):
    print("Model dosyası bulundu!")
  # Yükleme sırasında eksik ağırlıkları yok saymak
    model_gru.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')), strict=False)

else:
    print("Model dosyası bulunamadı!")

model_gru.eval()  # Modeli değerlendirme moduna al

# Loglama ayarları
logging.basicConfig(filename='api.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Tahmin endpoint'i
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Gelen veriyi al
        data = request.json
        logging.info(f"Gelen veri: {data}")

        # Giriş doğrulama
        if not data or 'features' not in data:
            logging.error("Geçersiz veri formatı. 'features' anahtarı bulunamadı.")
            return jsonify({'error': 'Geçersiz veri formatı. "features" anahtarı bulunamadı.'}), 400

        if len(data['features']) != 3:
            logging.error(f"Geçersiz veri uzunluğu. Beklenen: 3, Alınan: {len(data['features'])}")
            return jsonify({'error': 'Geçersiz veri uzunluğu. 3 özellik bekleniyor.'}), 400

        # Veriyi modele uygun hale getir
        input_data = np.array(data['features']).reshape(1, 1, -1)  # GRU için uygun şekil
        input_tensor = torch.tensor(input_data, dtype=torch.float32)

        # Tahmin yap
        with torch.no_grad():
            prediction = model_gru(input_tensor)
            prediction = (prediction > 0.5).float().item()

        # Tahmin sonucunu logla
        logging.info(f"Tahmin sonucu: {prediction}")

        # Tahmin sonucunu döndür
        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        # Hata durumunda logla
        logging.error(f"Hata: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(debug=True)
