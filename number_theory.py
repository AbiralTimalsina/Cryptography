import random

def miller_rabin(n, k=5):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_primitive_root(g, p):
    if pow(g, (p-1)//2, p) == 1:
        return False
    return True

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

# Example Usage
n = 37
print(f"Is {n} prime? {miller_rabin(n)}")

m = 10
print(f"Euler's Totient Function φ({m}) = {totient(m)}")

prime = 7
primitive_root = find_primitive_root(prime)
print(f"Primitive root of {prime}: {primitive_root}")