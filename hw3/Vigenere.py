# Understood and adapted from http://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python

from itertools import starmap, cycle

def encrypt(message, key):

    # convert to uppercase.
    # strip out non-alpha characters.
    # create autokey
    message = filter(lambda x: x.isalpha(), message.upper())
    autokey = key + message

    # single letter encrpytion.
    def enc(c,k): return chr(((ord(k) - ord('A') + ord(c) - ord('A')) % 26) + ord('A'))
    return "".join(starmap(enc, zip(message, autokey)))



def decrypt(message, key):

    # single letter decryption.
    # create autokey
    def dec(c,k): return chr(((ord(c) - ord(k)) % 26) + ord('A'))

    keylen = len(key)
    msgtext = ""
    for i in range(len(message)):
        if i < keylen:
	    k = key[i]
        else:
	    k = msgtext[i-keylen]
        msgtext += dec(message[i],k)

    return msgtext



if __name__ == "__main__":
	text = "LET US CHANGE OUR TRADITIONAL ATTITUDE TO THE CONSTRUCTION OF PROGRAMS"
	key = "ALGORITHMS"

	encr = encrypt(text, key)
	decr = decrypt(encr, key)

	print text     
	print encr 
	print decr
