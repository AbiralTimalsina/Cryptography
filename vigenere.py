plain_text= input("Enter plain text: ")
key= input("Enter key: ")
cipher_text=""
for i in range(len(plain_text)):
    if plain_text[i].isalpha():
        if plain_text[i].isupper():
            cipher_text += chr((ord(plain_text[i])-65+ord(key[i%len(key)])-65)%26+65)
        else:
            cipher_text += chr((ord(plain_text[i])-97+ord(key[i%len(key)])-97)%26+97)
    else:
        cipher_text += plain_text[i]
print("Cipher text: ",cipher_text)