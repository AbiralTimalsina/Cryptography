import numpy as np

def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [c for c in key + "".join([c for c in alphabet if c not in key])]
    return np.array(matrix).reshape(5, 5)

def find_position(matrix, letter):
    idx = np.where(matrix == letter)
    return idx[0][0], idx[1][0]

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"  # Padding
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            result += matrix[row_a, (col_a+1)%5] + matrix[row_b, (col_b+1)%5]
        elif col_a == col_b:
            result += matrix[(row_a+1)%5, col_a] + matrix[(row_b+1)%5, col_b]
        else:
            result += matrix[row_a, col_b] + matrix[row_b, col_a]
    return result

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    result = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            result += matrix[row_a, (col_a-1)%5] + matrix[row_b, (col_b-1)%5]
        elif col_a == col_b:
            result += matrix[(row_a-1)%5, col_a] + matrix[(row_b-1)%5, col_b]
        else:
            result += matrix[row_a, col_b] + matrix[row_b, col_a]
    return result

message = "HELLO WORLD"
key = "PLAYFAIR"
encrypted_message = playfair_encrypt(message, key)
decrypted_message = playfair_decrypt(encrypted_message, key)

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)