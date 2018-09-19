# Stack to find maximum j - i subject to 
# constraint A[i] < A[j]

class myStack:

	def __init__(self):
		self.array = []
		self.span = []

	def is_empty(self):
		return self.array == []

	def push(self, val):
		self.array.append(val)

	def pop(self):
		if not self.is_empty():
			return self.array.pop()
		else:
			return '$'
	def top(self):
		return self.array[-1]


def finding_span(A, n):

	s = list()
	d = myStack()
	for i in range(n):
		while (not d.is_empty()) and A[i] > A[d.top()]:
			d.pop()
		if d.is_empty():
			p = -1
		else:
			p = d.top()

		s.append(i - p)
		d.push(i)
	return s

A = [6, 3, 4, 5, 2]
n = 5
print(*finding_span(A, n))
