# Function to get maximum from a stack in O(1) time
import random

class Maximum:

	def __init__(self):
		self.array = []
		self.maximum = []

	def is_empty(self):
		return self.array == []

	def push(self, val):

		self.array.append(val)

		if (self.maximum == []) or (val >= self.maximum[-1]):
			self.maximum.append(val)
		else:
			self.maximum.append(self.maximum[-1])

	def pop(self):

		if not self.is_empty():
			self.array.pop()
			self.maximum.pop()
		else:
			return -1

	def get_max(self):
		return self.maximum[-1]

x = Maximum()

for i in range(10):
	x.push(random.randint(0,100))

print(*x.array)
print(x.get_max())