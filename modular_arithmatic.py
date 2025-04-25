# Python implementation of modular arithmetic concepts

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def additive_inverse(a, m):
    return (-a) % m

def multiplicative_inverse(a, m):
    if gcd(a, m) != 1:
        return None  # Inverse does not exist
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def is_relatively_prime(a, b):
    return gcd(a, b) == 1

# Example Usage
a = int (input("Enter a: "))
m = int (input("Enter m: "))
print(f"GCD of {a} and {m}: {gcd(a, m)}")
print(f"Additive Inverse of {a} mod {m}: {additive_inverse(a, m)}")
print(f"Multiplicative Inverse of {a} mod {m}: {multiplicative_inverse(a, m)}")
print(f"Are {a} and {m} relatively prime?: {is_relatively_prime(a, m)}")