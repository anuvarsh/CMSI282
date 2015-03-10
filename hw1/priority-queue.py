class PriorityQueue:

	def __init__(self):
		self.heap = []
		self.size = 0

	def add(self, x):
		self.heap.append(x)
		self.sift_up(len(self.heap)-1)
		self.size += 1
		return self

	def peek(self):
		return self.heap[0]

	def remove(self):
		if self.len == 0:
			raise ValueError "The queue is empty."
		if self.len == 1:
			self.heap = []
			self.size -= 1
		else: 
			self.heap[0] = self.heap.pop()
			sift_down(0)
			self.size -= 1
		return self

	def __len__(self):
		# return len(self.heap)
		# Or if we shouldn't use the len() function...
		return size

	def __str__(self):
		# return str(self.heap)
		# Or if we shouldn't use the str() function...
		return for p in self.heap: print p

	# Sift up the element at index i
	def sift_up(self, i):
		parent = (i - 1)
		if parent >= 0 and self.heap[parent] > self.heap[i]:
			self.heap[parent] = self.heap[i]
			self.heap[i] = self.heap[parent]
			self.sift_up(parent)

	# Sift down the element at index i
	def sift_down(self, i):
		child = (i * 2) + 1
		if child >= len(self.heap):
			return 
		if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
			child += 1
		if self.heap[i] > self.heap[child]:
			self.heap[child] = self.heap[i]
			self.heap[i] = self.heap[child]
			self.sift_down(child)












