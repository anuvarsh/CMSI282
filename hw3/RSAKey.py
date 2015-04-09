import time as tm 

class RSAKey:
	def __init__(self):
		self.prime_list = []

	def next_prime(self):
		if not self.prime_list:
			self.scanner = 2
			self.prime_list.append(self.scanner)
			return self.scanner

		found = False
		while not found:
			self.scanner += 1
			for i in self.prime_list:
				if self.scanner % i == 0:
					break
			else:
				found = True
		else:
			self.prime_list.append(self.scanner)
		return self.scanner

	def a_factor(self, q):
		self.prime_list = []
		mill = 0
		found = False
		while not found:
			p = self.next_prime()
			if p/1000 > mill:
				print 'tried up to', p
				mill += 1 
			if (q % p) == 0:
				found = True
		else:
			return p

	def egcd(self, a, b):
		if a == 0:
			return (b, 0, 1)
		else:
			g, y, x = self.egcd(b % a, a)
			return (g, x - (b // a) * y, y)

	def modinv(self, a, m):
		gcd, x, y = self.egcd(a, m)
		if gcd != 1:
			return None  # modular inverse does not exist
		else:
			return x % m

if __name__ == '__main__':
	#t1 = tm.time()
	RSAobject = RSAKey()
	n = 729880581317
	#n = 221
	#y = x.a_factor(n)
	#print y, n/y
	#t2 = tm.time()
	#print "took ", int(t2 - t1), " seconds"

	a = (822892*886968)
	e = 5
	print a
	print e
	answer = RSAobject.modinv(e,a)
	#answer = RSAobject.modinv(42,2017)
	print "d = ", answer



