## symmetric

import os
from Crypto.Cipher import AES

# Generating a random key
key = os.urandom(32)

# Encryption
plaintext = b'This is a secret message'

cipher = AES.new(key, AES.MODE_EAX)

ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Decryption
cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)

decrypted_message = cipher.decrypt(ciphertext)

print(decrypted_message)

## asymmetric

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = b"Network Security"

# Encrypt
encrypted = public_key.encrypt(
    message,
    padding.PKCS1v15()
)

print("Encrypted Message:", encrypted)

# Decrypt
decrypted = private_key.decrypt(
    encrypted,
    padding.PKCS1v15()
)

print("Decrypted Message:", decrypted.decode())