import hashlib

message = "Jon snow is the king in the north"

message = message.encode()

hashobj1 = hashlib.sha224(message)

hashobj2 = hashlib.sha256(message)

hashobj3 = hashlib.sha512(message)

print("SHA224: ", hashobj1.hexdigest())
print("SHA256: ", hashobj2.hexdigest())
print("SHA512: ", hashobj3.hexdigest())