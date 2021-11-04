from py_des import *
import random

message = "what on earth?"

key_11 = random.randrange(0,256)
key_1 = bytes([key_11, 0,0,0,0,0,0,0])

key_21 = random.randrange(0,256)
key_2 = bytes([key_21, 0,0,0,0,0,0,0])

print("originals", key_11, " ",key_21)

k1 = des(key_1, ECB, [0]*8, pad=None, padmode=PAD_PKCS5)
k2 = des(key_2, ECB, [0]*8, pad=None, padmode=PAD_PKCS5)

# alice sending the encrypted message
cipher = k1.encrypt(k2.encrypt(message))

# eve's attack on double des
lookup = {}
for i in range(256):
    key = bytes([i, 0,0,0,0,0,0,0])
    k = des(key, ECB, [0]*8, pad=None, padmode=PAD_PKCS5)
    lookup[k.encrypt(message)] = i

for i in range(256):
    key = bytes([i, 0,0,0,0,0,0,0])
    k = des(key, ECB, [0]*8, pad=None, padmode=PAD_PKCS5)
    if k.decrypt(cipher) in lookup:
        print("key21 ",lookup[k.decrypt(cipher)])
        print("key11 ",i)
        key_1 = bytes([i, 0,0,0,0,0,0,0])
        key_2 = bytes([lookup[k.decrypt(cipher)], 0,0,0,0,0,0,0])
        k1 = des(key_1, ECB, [0]*8, pad=None, padmode=PAD_PKCS5)
        k2 = des(key_2, ECB, [0]*8, pad=None, padmode=PAD_PKCS5)
        print("eve breaking double des",k2.decrypt(k1.decrypt(cipher)))
        break
