from frequency_analysis import Attack


original_string = "New applicants will now be required to complete a driving test based on the new scoring system.To pass the written portion of the driving exam, which has a total score of 100, an applicant must obtain 60 points out of a total of 100.The portion will ask objective questions from the DoTM's 500-question question bank, which has previously been released.Similarly, the trial phase will also be done using the new scoring system, in which the applicant must get 70 points in order to pass the trial.In comparison to previous trials, where an application was automatically disqualified if they made even a slight error, the new scoring system will provide much-needed respite to applicants.".lower()
original_key = {'a': 'm', 'b': 'c', 'c': 'n', 'd': 'h', 'e': 's', 'f': 'l', 'g': 'p', 'h': 'a', 'i': 'v', 'j': 'y', 'k': 'k', 'l': 'w', 'm': 'g', 'n': 't', 'o': 'i', 'p': 'o', 'q': 'z', 'r': 'b', 's': 'x', 't': 'e', 'u': 'u', 'v': 'q', 'w': 'd', 'x': 'r', 'y': 'f', 'z': 'j'}

def substitutionCaesar(key, string):
    caesar = ""
    for s in string:
        if(s not in key):
            caesar += s
            continue
        caesar += key[s]
    return caesar

print(substitutionCaesar(original_key, original_string))

cipher = "tsd moowvnmtex dvww tid cs bszuvbsh ei nigowses m hbvqvtp esxe cmxsh it eas tsd xnibvtp xfxesg.ei omxx eas dbveest oibevit il eas hbvqvtp srmg, davna amx m eiemw xnibs il 100, mt moowvnmte guxe icemvt 60 oivtex iue il m eiemw il 100.eas oibevit dvww mxk icysnevqs zusxevitx lbig eas hieg'x 500-zusxevit zusxevit cmtk, davna amx obsqviuxwf csst bswsmxsh.xvgvwmbwf, eas ebvmw oamxs dvww mwxi cs hits uxvtp eas tsd xnibvtp xfxesg, vt davna eas moowvnmte guxe pse 70 oivtex vt ibhsb ei omxx eas ebvmw.vt nigombvxit ei obsqviux ebvmwx, dasbs mt moowvnmevit dmx mueigmevnmwwf hvxzumwvlvsh vl easf gmhs sqst m xwvpae sbbib, eas tsd xnibvtp xfxesg dvww obiqvhs guna-tsshsh bsxoves ei moowvnmtex."
