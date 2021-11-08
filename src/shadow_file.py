import hashlib
import base64

def guess_password(salt, iterations, entropy):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c1 in alphabet:
        for c2 in alphabet:
            password = str.encode(c1+c2)
            value = base64.b64encode(hashlib.pbkdf2_hmac('sha512', password, salt, iterations, dklen=128))
            if value == entropy:
                return password

iterations = 45454
salt = base64.b64decode("abcd".encode())
validation = "SALTED-SHA512-PBKDF2"
entropy = """cY31dpDovYL1RClaIga025h/m7Q44vVR1iQgWGeWFxLM56f+K2Cw+5IvJxorDMzL/3OTTZxMogrI9sALLEfG9UShdrAZUo0M5WJTS0xmRiML2zaqgZRMk5wQ3bfmDZwBfmYCO2DedFuj8Fr5EjUWq5h8vzEGeNmqo6ZKo8+caHM=""".encode()

# supposing 2 character plaintext password for simplicity
# password =  "ab".encode()

password = guess_password(salt, iterations, entropy)
# value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
print(f"original entropy {entropy}")
# print(f" calculated hash : {base64.b64encode(value)}")
print(password)
