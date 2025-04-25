import numpy as np

def mod_inverse_matrix(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return (det_inv * adjugate) % modulus

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_cipher_encrypt(text, key_matrix):
    if len(text) % len(key_matrix) != 0:
        text += 'X'  # Padding if necessary
    vector = np.array(text_to_numbers(text)).reshape(-1, len(key_matrix))
    encrypted_vector = (np.dot(vector, key_matrix) % 26).flatten()
    return numbers_to_text(encrypted_vector)

def hill_cipher_decrypt(ciphertext, key_matrix):
    inverse_matrix = mod_inverse_matrix(key_matrix, 26)
    vector = np.array(text_to_numbers(ciphertext)).reshape(-1, len(key_matrix))
    decrypted_vector = (np.dot(vector, inverse_matrix) % 26).flatten()
    return numbers_to_text(decrypted_vector)

key_matrix = np.array([[3, 6], [1, 5]])
message = "MOVIE"
encrypted_message = hill_cipher_encrypt(message, key_matrix)
decrypted_message = hill_cipher_decrypt(encrypted_message, key_matrix)

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)