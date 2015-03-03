def mod_exp(a, b, p):
    if (b == 1): 
    	return a % p
    x = modexp(a, b>>1, p)
    x = (x * x) % p
    if (b & 1 == 1): 
    	x = (x * a) % p
    return x

def exp(b, c):
    if (c == 1): 
    	return b
    z = exp(b, c>>1)
    z = z * z
    if (c & 1 == 1): 
    	z = z * b
    return z

def complex_mod_exp(a, b, c, p):
    pow1 = exp(b, c)
    res = modexp(a, pow1, p)
    return res
