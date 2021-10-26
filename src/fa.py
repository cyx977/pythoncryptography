import operator
import sys
cipher = """tsd moowvnmtex dvww tid cs bszuvbsh ei nigowses m hbvqvtp esxe \n
cmxsh it eas tsd xnibvtp xfxesg.ei omxx eas dbveest oibevit il eas hbvqvtp \n
srmg, davna amx m eiemw xnibs il 100, mt moowvnmte guxe icemvt 60 oivtex \n
iue il m eiemw il 100.eas oibevit dvww mxk icysnevqs zusxevitx lbig eas\n
 hieg'x 500-zusxevit zusxevit cmtk, davna amx obsqviuxwf csst bswsmxsh.\n
 xvgvwmbwf, eas ebvmw oamxs dvww mwxi cs hits uxvtp eas tsd xnibvtp xfxesg, \n
 vt davna eas moowvnmte guxe pse 70 oivtex vt ibhsb ei omxx eas ebvmw.\n
 vt nigombvxit ei obsqviux ebvmwx, dasbs mt moowvnmevit dmx mueigmevnmwwf\n
  hvxzumwvlvsh vl easf gmhs sqst m xwvpae sbbib, eas tsd xnibvtp xfxesg \n
  dvww obiqvhs guna-tsshsh bsxoves ei moowvnmtex."""

class Attack:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.plain_chars_left = 'abcdefghijklmnopqrstuvwxyz'
        self.cipher_chars_left = 'abcdefghijklmnopqrstuvwxyz'
        self.freq = {}
        self.key = {}
        self.mappings = {}
        self.freq_english = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
               'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
               'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
               's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
               'y': 0.0197, 'z': 0.0007}
    
    def get_key(self):
        return self.key
    
    def calculate_freq(self, cipher):
        for c in self.alphabet:
            self.freq[c] = 0
        letter_count = 0
        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                letter_count += 1
        for c in self.freq:
            self.freq[c] = round(self.freq[c]/letter_count, 4)

    def print_freq(self):
        new_line_count = 0
        for c in self.freq:
            print(c, ":", " ", self.freq ," ", end="")
            if new_line_count % 3 == 2:
                print()
            new_line_count +=1

    def calculate_matches(self):
        for cipher_char in self.plain_chars_left:
            map = {}
            for plain_char in self.plain_chars_left:
                map[plain_char] = round(abs(self.freq[cipher_char] - self.freq_english[plain_char]), 4)
            self.mappings[cipher_char] = sorted(map.items(), key= operator.itemgetter(1))
    
    def set_known_key(self, cipher_char, plain_char):
        if cipher_char not in self.cipher_chars_left or plain_char not in self.plain_chars_left:
            print("key couldn't be mapped due to collission")
            sys.exit(-1)
        self.key[cipher_char] = plain_char
        self.plain_chars_left = self.plain_chars_left.replace(plain_char, '')
        self.cipher_chars_left = self.cipher_chars_left.replace(cipher_char, '')

    def guess_key(self):
        for cipher_char in self.cipher_chars_left:
            for plain_char, diff in self.mappings[cipher_char]:
                if plain_char in self.plain_chars_left:
                    self.key[cipher_char] = plain_char
                    self.alphabet = self.alphabet.replace(plain_char, '')
                    break


def decrypt(key, cipher):
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    return message


attack = Attack()
attack.calculate_freq(cipher)
print()

print(attack.freq)

attack.calculate_matches()

attack.set_known_key('c', 'b')
attack.set_known_key('s', 'e')
attack.set_known_key('d', 'w')
attack.set_known_key('x', 's')
attack.set_known_key('a', 'h')
attack.set_known_key('f', 'y')
attack.set_known_key('b', 'r')
attack.set_known_key('v', 'i')
attack.set_known_key('m', 'a')
attack.set_known_key('h', 'd')
attack.set_known_key('p', 'g')
attack.set_known_key('o', 'p')
attack.set_known_key('z', 'q')
attack.set_known_key('u', 'u')
attack.set_known_key('r', 'x')
attack.set_known_key('l', 'f')
attack.set_known_key('k', 'k')























key = attack.guess_key()
print(decrypt(attack.get_key(), cipher))
print(attack.get_key())








# attack.print_freq()
# print()

# for c in attack.mappings:
#     print(c, " : ", attack.mappings[c])
