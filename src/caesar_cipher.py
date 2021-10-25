#BRX DUH DZHVRPH 
#key 3
#YOU ARE AWESOME
from enum import Enum;
letters = "abcdefghijklmnopqrstuvwxyz";

class CaesarEnum(Enum):
    enc = 1;
    dec = 2;

def genKey(n):
    key = {};
    count = 0;
    for c in letters:
        key[c] = letters[(count + n) % len(letters)]
        count += 1;
    return key;

def caesar(n, string, method):
    key = {};
    if(method == CaesarEnum.enc):
        key = genKey(n);
    else:
        key = genKey(n * -1);
    caesar = ""
    for s in string:
        if(s not in key):
            caesar += s;
            continue;
        caesar += key[s];
    return caesar;

n = 3
print(caesar(n, "you are awesome", CaesarEnum.enc))
print(caesar(n, caesar(n, "you are awesome", CaesarEnum.enc), CaesarEnum.dec))