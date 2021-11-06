# def hcf(a,b):
#     if(b==0):
#         return a
#     else:
#         return hcf(b,a%b)

# print ("The gcd of 60 and 48 is : ",end="")
# print (hcf(60,48))

# generator
# g = 14
# m = 9
# satisfies = True

# lookup = {}
# for i in range(m-1):
#     lookup[i] = g**i % m
# values = list(lookup.values())
# print(values)

# flag = True
# for i in range(1,m):
#     if i not in values:
#         flag = False

# print(flag)


def leastGenFinder(generator, prime):
    lookup = {}
    for i in range(prime-1):
        lookup[i] = generator**i % prime

    values = list(lookup.values())
    print(values)

    flag = True
    # excluding zero
    for i in range(1,prime):
        if i not in values:
            flag = False 
    return flag

# modulus should be a prime number
found = False
prime = 1889
generator = 1502
while not found:
    print("trying with ", generator)
    found = leastGenFinder(generator, prime)
    if found:
        break
    else:
        generator += 1
print(f"found generator for prime {prime} : {generator}")