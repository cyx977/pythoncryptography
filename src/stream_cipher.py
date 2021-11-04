import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key
 
    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2**31
        return self.next
 
    def get_key_byte(self):
        return (self.rand() // 2**23) % 256
 
 
def encrypt(key, message):
    return bytes(message[i] ^ key.get_key_byte() for i in range(len(message)))
 

# data lost mimic during transmission
def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0, 8)
        b.append(c)
    return bytes(b)

def modification(cipher):
    mod = [0]*len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes(mod[i] ^ cipher[i] for i in range(len(cipher)))

def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])

def crack(key_string, cipher):
    length = min(len(key_string), len(cipher))
    return bytes(key_string[i] ^ cipher[i] for i in range(length))

def brute_force(plain, cipher):
    for k in range(2**31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            return k
    return False


# # this is alice
# key = KeyStream(10)
# message = "send bob:   10$".encode()
# cipher = encrypt(key, message)
# print(cipher)

# #this is bob
# cipher = modification(cipher)

# key = KeyStream(10)
# print("decoded", encrypt(key, cipher))



# #reusing keys
# #eve goes to alice
# eves_message = "this is eve's most valued secret of all her life".encode()

# #this is alice alone
# key = KeyStream(10)
# message = eves_message;
# cipher = encrypt(key, message)
# print(cipher)

# # this is eve(alone1) all evil 
# eves_key_stream = get_key(eves_message, cipher)

# #this is bob
# key = KeyStream(10)
# message = encrypt(key, cipher)
# print(message)

# # alice again
# message = "Hi bob, let's meet and plan for our secret stuff".encode()
# key = KeyStream(10)
# cipher = encrypt(key, message)
# print(cipher)

# # #bob again
# key = KeyStream(10)
# message = encrypt(key, cipher)
# print(message)

# # #eve again (more evil than again)
# print("This is eve")
# print(crack(eves_key_stream, cipher))

# this is alice
secret_key = random.randrange(0, 2**20)
key = KeyStream(secret_key)
print("alice's secret key", secret_key)
header = "Message: "
message =  header + "my secret message to bob"
message = message.encode()
print(message)
cipher = encrypt(key, message)
print(cipher)

# this is bob
key = KeyStream(secret_key)
message = encrypt(key, cipher)
print(message)

# this is eve
print("bruting")
bf_key = brute_force(header.encode(), cipher)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
print(message)
print("eve's bruteforce key is ",bf_key)





