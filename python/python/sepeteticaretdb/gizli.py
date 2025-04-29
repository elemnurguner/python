import os

# 24 byte'lık rastgele bir anahtar oluştur
secret_key = os.urandom(24).hex()
print(secret_key)