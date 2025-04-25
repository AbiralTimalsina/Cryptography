import hashlib

def md5_hash(text):
    md5_text = hashlib.md5()
    md5_text.update(text.encode('utf-8'))
    return md5_text.hexdigest()

# if __name__ == '__main__':
input_text = input('Enter the text: ')
print('MD5 hash:', md5_hash(input_text))