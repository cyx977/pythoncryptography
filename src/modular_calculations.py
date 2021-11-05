# def checkPrime(n):
#     counter = 0
#     for i in range(1,n):
#         if n % i == 0:
#             counter += 1
#             # print(n ," divisible by ",i)
#     # print(counter)
#     if(counter > 1):
#         return False
#     else:
#         return True

# for i in range(100):
#     if checkPrime(i):
#         print(i)


# def hcf(a,b):
#     if(b==0):
#         return a
#     else:
#         return hcf(b,a%b)
  
# a = 60
# b= 48
  
# # prints 12
# print ("The gcd of 60 and 48 is : ",end="")
# print (hcf(60,48))

# 4+ 7 mod 12
# val = (14+15) % 12
# print(val)

# 4*5 mod 12
# val = 4*5 %12
# print(val)

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


def leastGenFinder(generator, modulus):
    lookup = {}
    for i in range(modulus-1):
        lookup[i] = generator**i % modulus

    values = list(lookup.values())
    print(values)

    flag = True
    # excluding zero
    for i in range(1,modulus):
        if i not in values:
            flag = False 
    return flag

# should be a prime number
found = False
modulus = 41
generator = 23
while not found:
    print("trying with ", generator)
    found = leastGenFinder(generator, modulus)
    if found:
        break
    else:
        generator += 1
print("found generator ",generator)