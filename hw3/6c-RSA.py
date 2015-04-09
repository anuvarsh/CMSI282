# a^b mod p
def mod_exp(a, b, p):
    if (b == 1): 
    	return a % p
    x = mod_exp(a, b>>1, p)
    x = (x * x) % p
    if (b & 1 == 1): 
    	x = (x * a) % p
    return x

def verify(n, e, s, m):
	x = mod_exp(s, e, n)
	return x == m 

if __name__ == "__main__":
	#p = 11
	#q = 13
	n = 143
	e = 7
	d = 103
	m = "anu"
	s = [0, 0, 0]
	for i in range(len(m)):
		s[i] = mod_exp(ord(m[i]), d, n) #the mapping is done by convering the character to integers with ord()
		print s[i]
	for i in s:
		print chr(mod_exp(i, e, n)) #this proves that (m1)^e = m mod n, and converts the integer back to a character for comparing convenience
	#print verify(n, e, s, m)


