from frequency_analysis import Attack, decrypt
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