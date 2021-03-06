import operator
import sys
cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

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
        cipher = cipher.lower()
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
    
if __name__ == "__main__":
    attack = Attack()
    attack.calculate_freq(cipher)
    attack.calculate_matches()
    attack.set_known_key('r', 'e')
    attack.set_known_key('v', 'c')
    attack.set_known_key('m', 'a')
    attack.set_known_key('p', 'h')
    attack.set_known_key('w', 'i')
    attack.set_known_key('k', 'n')
    attack.set_known_key('x', 'f')
    attack.set_known_key('d', 'd')
    attack.set_known_key('t', 'y')
    attack.set_known_key('q', 'k')
    attack.set_known_key('o', 'g')
    attack.set_known_key('y', 'm')
    attack.set_known_key('u', 'r')
    attack.set_known_key('c', 'w')
    attack.set_known_key('s', 'p')
    attack.set_known_key('a', 'x')
    attack.set_known_key('f', 'q')
    attack.set_known_key('g', 'z')


    key = attack.guess_key()
    print(decrypt(attack.get_key(), cipher))
    print(attack.get_key())







# attack.print_freq()
# print()

# for c in attack.mappings:
#     print(c, " : ", attack.mappings[c])
