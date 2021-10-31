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
message = """Facebook Inc. is now called Meta Platforms Inc., or Meta for short, to reflect what CEO Mark Zuckerberg said Thursday is its commitment to developing the new surround-yourself technology known as the " metaverse." But the social network itself will still be called Facebook. Also unchanged, at least for now, are its chief executive and senior leadership, its corporate structure and the crisis that has enveloped the company.Skeptics immediately accused the company of trying to change the subject from the Facebook Papers, the trove of leaked documents that have plunged it into the biggest crisis since it was founded in Zuckerberg's Harvard dorm room 17 years ago. The documents portray Facebook as putting profits ahead of ridding its platform of hate, political strife and misinformation around the world."""
key = genKey()
print(key)
cipher = substitutionCaesar(key, message)
print(cipher)
inv_map = {v: k for k, v in key.items()}
print(substitutionCaesar(inv_map, cipher));


# cipher = substitutionCaesar(key, "you are awesome")
# print(cipher)
# inv_map = {v: k for k, v in key.iteritems()}
# print(substitutionCaesar(inv_map, cipher));