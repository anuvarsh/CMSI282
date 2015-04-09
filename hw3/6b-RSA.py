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
	#q = 5
	n = 55
	e = 3
	d = 27
	m = 12
	s = mod_exp(m, d, n)
	print verify(n, e, s, m)
