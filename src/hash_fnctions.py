import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

m =  "this is a top secret".encode()

sha256 = hashlib.sha256()
sha256.update(m)
data = sha256.digest()

print(data)
print(modify(m))