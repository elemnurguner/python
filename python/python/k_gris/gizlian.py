import secrets

# 32 byte uzunluğunda bir secret key oluştur
secret_key = secrets.token_hex(12)

print(secret_key)
