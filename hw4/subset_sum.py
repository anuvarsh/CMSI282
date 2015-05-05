#this computes values of "is there a subset of length i, which sums to s"
#Q(i,s) := Q(i-1,s) || (x[i] == s) || Q(i-1,s-x[i])
def Q(i,s,A,B,prevQvalues):
	if ((s<A) or (s>B)):
		return False

	if (((s-x[i]) < A) or ((s-x[i]) > B)):
		res = prevQvalues[(i-1,s)] or (x[i] == s) # skip Q(i-1,s-x[i]) as it is False
	else:
		res = prevQvalues[(i-1,s)] or (x[i] == s) or prevQvalues[(i-1),(s-x[i])]

	return res

def app(x, target_sum):
	A = 0
	B = 0

	for i in range(len(x)):
		if (x[i] < 0):
			A += x[i]
		else:
			B += x[i]

	N = len(x);

	prevQvalues = {}
	for j in range(A, B+1):
		prevQvalues[(0,j)] = (x[0] == j)

	for i in range(1,N):
		for j in range(A, B+1):
			prevQvalues[(i,j)] = Q(i,j,A,B,prevQvalues)

	return Q(N-1,target_sum,A,B,prevQvalues)


if __name__ == '__main__':	
	x = [1,4,6,8,5]
	target_sum = 16
	print "Given list = ", x, ",  Target sum = ", target_sum
	print "the result is..."
	print app(x, target_sum)

