from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
import os

admin = Admin(name="Film Yönetimi", template_mode="bootstrap4")

# static klasörünün yolunu al
path = os.path.join(os.path.dirname(__file__), "static")

# Eğer static klasörü yoksa oluştur
if not os.path.exists(path):
    os.makedirs(path)

# FileAdmin ekleme fonksiyonu (app sonradan eklenecek)
def init_admin(app):
    admin.init_app(app)
    admin.add_view(FileAdmin(path, "/static/", name="Dosya Yönetimi"))
