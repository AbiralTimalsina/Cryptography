from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# Function to generate a random AES key
def generate_key():
    return get_random_bytes(16)

# Function to encrypt a message using AES CBC mode
def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return cipher.iv + ciphertext

# Function to decrypt a message using AES CBC mode
def decrypt(encrypted_data, key):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

# Example Usage
key = generate_key()
print(f"Generated key (hex): {key.hex()}")

message = input("Enter your message: ")
encrypted_data = encrypt(message, key)
print(f"Encrypted data (hex): {encrypted_data.hex()}")

decrypted_data = decrypt(encrypted_data, key)
print(f"Decrypted data: {decrypted_data}")