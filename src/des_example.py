from py_des import *


# message = "hello world".encode()
# key = "DESCRYPT"
# iv = bytes([1]*8)
# k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

# cipher = k.encrypt(message)
# print("length of plain_text : ", len(message))
# print("length of cipher : ", len(cipher))
# print("Encrypted complete cipher : ", cipher)

# print("Encrypted : ", cipher[0:8])
# print("Encrypted : ", cipher[8:16])
# print("Encrypted : ", cipher[16:24])
# print("Decrypted : ", k.decrypt(cipher).decode())

def modify(cipher):
    mod = [0]*len(cipher)
    mod[8] = ord('1')
    # mod[10] = ord(' ') ^ ord('1')
    # mod[11] = ord(' ') ^ ord('1')
    # mod[12] = ord('1') ^ ord('0')
    return bytes(mod[i] ^ cipher[i] for i in range(len(cipher)))

message = "send bob:   10$ and send them to him"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, ECB, iv,pad=None, padmode=PAD_PKCS5)




# alice sending the encrypted message
cipher = k.encrypt(message)
print("length of plain_text : ", len(message))
print("length of cipher : ", len(cipher))
print("Encrypted complete cipher : ", cipher)
print(k.decrypt(cipher))


# bob modifying the cipher text
# cipher = modify(cipher)

#bank decodes the message
print(k.decrypt(cipher))


