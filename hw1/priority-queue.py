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

import unittest
import random

class PriorityQueueTestCase(unittest.TestCase):

    def test_new_priority_queues_are_empty(self):
        q = PriorityQueue()
        self.assertEqual(len(q), 0)
        self.assertEqual(str(q), '[]')

    def test_remove_from_new_priority_queue_raises(self):
        q = PriorityQueue()
        self.assertRaises(q.remove)

    def test_peek_works_on_one_element_queue(self):
        q = PriorityQueue()
        q.add(7)
        self.assertEqual(q.peek(), 7)
        self.assertEqual(len(q), 1)
        self.assertEqual(str(q), '[7]')

    def test_add_then_remove_on_empty_queue_returns_to_empty(self):
        q = PriorityQueue()
        q.add(7)
        self.assertEqual(len(q), 1)
        q.remove()
        self.assertEqual(len(q), 0)

    def test_one_hundred_adds_and_removes(self):
        q = PriorityQueue()
        items = [i for i in range(100)]
        random.shuffle(items)
        for item in items:
            q.add(item)
        for item in range(100):
            self.assertEqual(q.peek(), item)
            q.remove()

    def test_operation_and_stringification_all_together_because_i_am_lazy(self):
        q = PriorityQueue()
        q.add(8)
        q.add(3)
        self.assertEqual(str(q).replace(' ', ''), '[3,8]')
        q.add(1)
        self.assertEqual(str(q).replace(' ', ''), '[1,8,3]')
        q.remove()
        self.assertEqual(str(q).replace(' ', ''), '[3,8]')

if __name__ == '__main__':
    unittest.main()










