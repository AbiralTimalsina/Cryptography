def ceaser_cipher(plain_text, key):
    cipher_text=""
    for i in plain_text:
        if i.isalpha():
            if i.isupper():
                cipher_text += chr((ord(i)-65+key)%26+65)
            else:
                cipher_text += chr((ord(i)-97+key)%26+97)
        else:
            cipher_text += i
    return cipher_text


plain_text= input("Enter plain text: ")
key= int(input("Enter key: "))

cipher_text= ceaser_cipher(plain_text, key)
print("Cipher text: ",cipher_text)
print("Decryption of the above cipher text is: ",ceaser_cipher(cipher_text, -key))