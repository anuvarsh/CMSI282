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


if __name__ == '__main__':
	t1 = tm.time()
	x = RSAKey()
	n = 729880581317
	#n = 221
	y = x.a_factor(n)
	print y, n/y
	t2 = tm.time()
	print "took ", int(t2 - t1), " seconds"




