#BRX DUH DZHVRPH 
#key 3
#YOU ARE AWESOME
letters = "abcdefghijklmnopqrstuvwxyz";

def genKey(n):
    key = {};
    count = 0;
    for c in letters:
        key[c] = letters[(count + n) % len(letters)]
        count += 1;
    return key;

def genCaesar(n, string):
    key = genKey(n);
    caesar = "";
    for s in string:
        if(s not in key):
            caesar += s;
            continue;
        caesar += key[s];
    return caesar;

def decryptCaesar(n, string):
    key = genKey(-n);
    caesar = ""
    for s in string:
        if(s not in key):
            caesar += s;
            continue;
        caesar += key[s];
    return caesar;
    
print(genCaesar(3,  "you are awesome"));
print(decryptCaesar(3, genCaesar(3,  "you are awesome")));