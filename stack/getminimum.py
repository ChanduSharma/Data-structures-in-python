# Stack to get minimum in O(1) i.e constant time

import random

class Minimum:

	def __init__(self):
		self.array = []
		self.minimum = []


	def is_empty(self):
		return self.array == []

	def push(self, val):

		self.array.append(val)
		if (self.minimum == []) or (val <= self.minimum[-1]):
			self.minimum.append(val)
		else:
			self.minimum.append(self.minimum[-1])

	def pop(self):

		if not self.is_empty():
			self.array.pop()
			self.minimum.pop()
		else:
			return '$'

	def get_min(self):
		return self.minimum[-1]


x = Minimum()

for i in range(10):
	x.push(random.randint(0,100))

print(*x.array)
print(x.get_min())

