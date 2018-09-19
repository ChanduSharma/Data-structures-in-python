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


	def pop(self):

		if not self.is_empty():
			a = self.array.pop()
			if a == self.minimum[-1]:
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

 