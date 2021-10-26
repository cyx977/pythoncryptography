import random

def genKey():
    letters = "abcdefghijklmnopqrstuvwxyz"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0,len(cletters)-1))
    return key

def substitutionCaesar(key, string):
    caesar = ""
    for s in string:
        if(s not in key):
            caesar += s
            continue
        caesar += key[s]
    return caesar

key = genKey()
cipher = substitutionCaesar(key, "you are awesome")
print(cipher)
inv_map = {v: k for k, v in key.iteritems()}
print(substitutionCaesar(inv_map, cipher));