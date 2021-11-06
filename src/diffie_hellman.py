import math
import random

def checkPrime(n):
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_prime(size):
    while True:
        p = random.randrange(size, size *2)
        if checkPrime(p):
            return p

def is_generator(g, p):
    for i in range(1, p - 1):
        if (g**i) % p ==1:
            return False
    return True

def get_generator(p):
    for g in range(2,p):
        if is_generator(g, p):
            return g

p = get_prime(10000)
g = get_generator(p)
print("Generator ",g," Prime ", p )

#alice
a = random.randrange(0,p)
g_a = (g**a) % p
#alice sends this out in the public
print(f"alice's g_a: {g_a}")

#bob
b = random.randrange(0, p)
g_b = (g**b) % p
#bob sends this out in the public
print(f"Bob's g_b {g_b}")

# back to alice
g_ab = (g_b**a) % p
print(f"g_ab {g_ab}")

# back to bob
g_ba = (g_a**b) % p
print(f"g_ba {g_ba}")