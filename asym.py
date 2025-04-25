import random
from sympy import mod_inverse, isprime

def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    key_A = pow(B, a, p)
    key_B = pow(A, b, p)
    return key_A, key_B

# Example Usage
dh_p, dh_g, dh_a, dh_b = 23, 5, 6, 15
key_A, key_B = diffie_hellman(dh_p, dh_g, dh_a, dh_b)
print(f"Diffie-Hellman Shared Key: {key_A}, {key_B}")

# RSA Implementation
def rsa_generate_keys():
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def rsa_encrypt(msg, pub_key):
    e, n = pub_key
    return pow(msg, e, n)

def rsa_decrypt(cipher, priv_key):
    d, n = priv_key
    return pow(cipher, d, n)

rsa_pub, rsa_priv = rsa_generate_keys()
cipher = rsa_encrypt(42, rsa_pub)
print(f"RSA Encrypted: {cipher}")
decrypted = rsa_decrypt(cipher, rsa_priv)
print(f"RSA Decrypted: {decrypted}")

# Elgamal Implementation
def elgamal_encrypt(p, g, y, msg, k):
    c1 = pow(g, k, p)
    c2 = (msg * pow(y, k, p)) % p
    return c1, c2

def elgamal_decrypt(p, x, c1, c2):
    s = pow(c1, x, p)
    s_inv = mod_inverse(s, p)
    return (c2 * s_inv) % p

elg_p, elg_g, elg_x = 97, 5, 36
elg_y = pow(elg_g, elg_x, elg_p)
k = 29
msg = 20
c1, c2 = elgamal_encrypt(elg_p, elg_g, elg_y, msg, k)
print(f"Elgamal Encrypted: ({c1}, {c2})")
decrypted = elgamal_decrypt(elg_p, elg_x, c1, c2)
print(f"Elgamal Decrypted: {decrypted}")