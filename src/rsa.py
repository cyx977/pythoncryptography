import math
import random
def is_prime(p):
    for i in range(2,math.isqrt(p)):
        if p % i == 0:
            return False
    return True

def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p

def lcm(p,q):
    return abs((p) * (q))//math.gcd(p, q)

def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False

def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False

def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p,n//p

# key generation
# step 1: generate two distinct primes
size = 1024
p = get_prime(size)
q = get_prime(size)
print(f"generated primes, {p} {q}")
# step 2: compute n = p*q
n = p * q
print(f"Modulus n: {n}")
# step 3: compute Carmichale's totient function lambda(n) = lcm(p-1, q-1)
# lcm(a,b) = abs(a*b)/gcd(a,b)
lambda_n = lcm(p-1,q-1)
print(f"lambda_n: {lambda_n}")
# step 4: choose and integer e such that 1 < e < lambda(n) and gcd(e, lambda(n)) = 1; 
# that is e and lambda(n) are coprime
e = get_e(lambda_n)
print(f"public exponent: {e}")
# step 5: determine d = e^-1 mod(lambda(n)); d is modular multiplicative inverse of e modulo lambda(n)
d = get_d(e, lambda_n)
print(f"Private d: {d}")
# done with key generation
print(f"public key(e,n) ({e},{n})")
print(f"private key d {d}")

# this is bob wanting to send a message
m = 390001
c = m**e % n
print(f"bob sends {c}")

# this is alice decrypting the cipher
m = c**d % n
print(f"decrypted by alice with his private key {m}")

# this is eve
print("eve sees the following: ")
print(f"public key (e,n) ({e},{n})")
print(f"encrypted cipher {c}")
p, q = factor(n)
print(f"Eve's factors p and q {p},{q}")
lambda_n = lcm(p-1, q-1)
d=get_d(e, lambda_n)
print(f"eve's secret exponent {d}")
m = c ** d % n
print(f"eve's attacked message: {m}")

# this is bob not being careful
print("this is bob not being careful")
message = "alice is awesome"
for m_c in message:
    c = ord(m_c)**e %n
    print(c,  " ", end="")

# now eve can do frequency analysis
