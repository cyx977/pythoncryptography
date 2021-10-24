#BRX DUH DZHVRPH 
#key 3
#YOU ARE AWESOME

def genCaesar(n, string):
    letters = "abcdefghijklmnopqrstuvwxyz";
    key = {};
    count = 0;
    for c in letters:
        key[c] = letters[(count + n) % len(letters)]
        count += 1;
    caesar = "";
    for s in string:
        if(s == " "):
            caesar += " ";
            continue;
        caesar += key[s];
    return caesar;


    
print(genCaesar(3,  "you are awesome"));