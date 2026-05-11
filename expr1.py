from cryptography.fernet import Fernet

message = "Winter is coming!"

key = Fernet.generate_key()

fernet = Fernet(key)

encrpted_message = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encrpted_message)

decrypted_message = fernet.decrypt(encrpted_message).decode()

print("decrypted string: ", decrypted_message)