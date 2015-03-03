def modexp(a, b, c, p):
	if(b==1): return a%p
	x = modexp(a,b>>1,p)
	x = (x*x)%p
	if(b&1==1)==1: # for odd number
        x = (x*a)%p
return x

def exp(b, c):
	if (c==1): return b
	x = 

