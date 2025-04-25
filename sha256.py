import hashlib

def sha256_hash(text):
    sha256_text = hashlib.sha256()
    sha256_text.update(text.encode('utf-8'))
    return sha256_text.hexdigest()

if __name__ == '__main__':
    input_text = input('Enter the text to hash: ')
    print('SHA256 hash:', sha256_hash(input_text))