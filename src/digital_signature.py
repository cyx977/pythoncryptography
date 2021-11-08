import hashlib

e = 7
n = 2892059
d = 412663

# this is the message that alice wants to sign and send to bob
message = "Bob you are awesome".encode()

# step1: hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n 
print(f"hash value {h}")
# step2 : decrypt the hash value (use secret exponent)
sign = h**d % n
print(message, sign)

# bob verifying the signature
#   step x.1 calculate the hash value of the messgae
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, 'big') % n 
print(f"hash value {h}")
#   step x.2 verify the signature
verification = sign**e % n
print(f"verification value {verification}")
