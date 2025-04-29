from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Anahtar ve IV (Initialization Vector) oluşturma
def generate_key_iv():
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)   # 128-bit IV
    return key, iv

# Veriyi şifreleme
def encrypt(plaintext, key, iv):
    # Padding ekleme (AES blok boyutu 128 bit olduğu için)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Şifreleme işlemi
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

# Veriyi çözme
def decrypt(ciphertext, key, iv):
    # Çözme işlemi
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Padding kaldırma
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

# Örnek kullanım
if __name__ == "__main__":
    key, iv = generate_key_iv()
    plaintext = "Bu bir gizli mesajdır."

    # Şifreleme
    ciphertext = encrypt(plaintext, key, iv)
    print(f"Şifrelenmiş veri: {ciphertext}")

    # Çözme
    decrypted_text = decrypt(ciphertext, key, iv)
    print(f"Çözülmüş veri: {decrypted_text}")