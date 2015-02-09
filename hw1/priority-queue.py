class PriorityQueue:

	def __init__(self):
		self.heap = [None] * 1000000 
		# heap arbitrarily set to have max size of 1,000,000

	def add(self, x):
		self.append(x)
		self.sift-up(len(self.heap)-1)
		return self

	def peek(self):
		return self.heap[0]

	def remove(self):
		if self.len == 0:
			raise ValueError, "It was empty."
		if self.len == 1:
			self.heap = []
		else: 
			self.heap[0] = None
			sift_down(0)
		return self

	def __len__(self):
		self.heap.len()

	def __str__(self):
		self.heap.str()

	# Sift up the element at index i
	def sift_up(self, i):
		parent = math.floor((i - 1)/2)
		if parent >= 0 and self.heap[parent] > self.heap[i]:
			self.heap[parent] = self.heap[i]
			self.heap[i] = self.heap[parent]
			sift_up(parent)

	# Sift down the element at index i
	def sift_down(self, i):
		child = math.floor((i * 2) + 1)
		if child >= self.heap.len:
			return 
		if child + 1 < self.heap.len and self.heap[child] > self.heap[child + 1]:
			child += 1
		if self.heap[i] > self.heap[child]:
			self.heap[child] = self.heap[i]
			self.heap[i] = self.heap[child]
			sift_down(child)












