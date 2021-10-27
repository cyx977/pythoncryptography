provided no enemy;  
alice can send unencrypted plaintext message to bob  
but eve could be around.  
that is why encrypt the message and send it to mike  

alice and bob can have a common key.  
with a caesar cipher and a key; they can transmit data which has no meaning to eve  
now eve doesnt understand alice and bob, he tries to decrypt the jibberish message.  
current implementation of our caesar can be decrypted easily.  
however;  

kerckoff's principle: Eve should not be able to break the ciphers even when he knows the cipher algorithm 
the attacker even if he know the algorithm(not the key); he shouldn't be able to decrypt it.  

rule of thumb is to use substitution cipher instead of shifting cipher. this leaves the pool of 26! permutatins.  
now lets use the frequency analysis  

one time pad uses xor to encrypt the data. key stream should not be reused.  
however one time pad is not practical.  
we have stream cipher to the rescue