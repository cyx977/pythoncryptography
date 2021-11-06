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

p = get_prime(100)
g = get_generator(p)
print("Generator ",g," Prime ", p )

