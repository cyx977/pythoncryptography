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
entropy = """mhwDYoFPBvfghTkpKqaEGUyjzICmPzY8CKuZGOad0Sz/7XPOTWNrlpVIfoz53oxsxXFo+toVp9FCTZo5dv00Ztf63GgxrSHsRQg7sJ2BF6G7sEU3ujD6CnSzd923vPNLodBN1RTqpIU67VebSQBobyEveSalInIrSY/CJ24i8uA=""".encode()

password =  "unstealablePassword@2@".encode()

value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
print(f"original entropy {entropy}")
print(f" calculated hash : {base64.b64encode(value)}")
