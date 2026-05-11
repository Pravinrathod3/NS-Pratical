## Python program to implement Caesar Cipher for encryption and decryption of text

def encrypt_text(plaintext, n):
    ans = ""

    for i in range(len(plaintext)):
        ch = plaintext[i]

        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)

    return ans

def decrypt_text(ciphertext, n):
    ans = ""

    for i in range(len(ciphertext)):
        ch = ciphertext[i]

        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) - n - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) - n - 97) % 26 + 97)

    return ans


plaintext = "HELLO EVERYONE"
n = 3

print("Plain Text is :", plaintext)
print("Shift pattern is :", n)
encrypt = encrypt_text(plaintext, n)
print("Cipher Text is :", encrypt)
decrpt = decrypt_text(encrypt, n)
print("Decrypted Text is :", decrpt)


## program to implement subsitution Cipher for encryption and decryption of text

import string

all_letters = string.ascii_letters

dict1 = {}
key = 4

# encryption mapping
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]

plain_txt = "I am studying Data Encryption"

cipher_txt = []

for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        cipher_txt.append(char)

cipher_txt = "".join(cipher_txt)

print("Cipher Text is:", cipher_txt)

# decryption mapping
dict2 = {}

for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i - key) % len(all_letters)]

decrypt_txt = []

for char in cipher_txt:
    if char in all_letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        decrypt_txt.append(char)

decrypt_txt = "".join(decrypt_txt)

print("Recovered plain text :", decrypt_txt)