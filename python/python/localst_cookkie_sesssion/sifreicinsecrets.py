import secrets

# 32 karakterlik güvenli bir secret key oluşturma
secret_key = secrets.token_hex(16)  # 16 bayt = 32 karakter
print("Oluşturulan Secret Key:", secret_key)