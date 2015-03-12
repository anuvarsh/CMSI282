class PriorityQueue:

	def __init__(self):
		self.heap = []

	def add(self, x):
		self.heap.append(x)
		self.sift_up(len(self.heap)-1)
		return self

	def peek(self):
		if len(self.heap) == 0:
			raise ValueError, "The queue is empty."
		return self.heap[0]

	def remove(self):
		test_empty = self.peek()
		if len(self.heap) == 1:
			self.heap = []
		else:
			self.heap[0] = self.heap.pop()
			self.sift_down(0)
		return self

	def __len__(self):
		return len(self.heap)

	def __str__(self):
		return str(self.heap)

	# Sift up the element at index i
	def sift_up(self, i):
		parent = int((i - 1)/2)
		if parent >= 0 and self.heap[parent] > self.heap[i]:
			self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
			self.sift_up(parent)

	# Sift down the element at index i
	def sift_down(self, i):
		child = (i * 2) + 1
		if child >= len(self.heap):
			return 
		if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
			child += 1
		if self.heap[i] > self.heap[child]:
			self.heap[child], self.heap[i],  = self.heap[i], self.heap[child]
			self.sift_down(child)









