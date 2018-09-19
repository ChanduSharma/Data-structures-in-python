class Conversion:

	def __init__(self):
		self.array = []
		self.output = []
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

	def is_empty(self):
		return self.array == []

	def peek(self):
		return self.array[-1]

	def push(self, val):

		self.array.append(val)

	def pop(self):

		if self.array:
			return self.array.pop()
		else:
			return '$'

	def is_operand(self, ch):
		return ch.isalpha()

	def not_greater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	def infix_to_postfix(self, expression):

		for i in expression:

			if self.is_operand(i):
				self.output.append(i)

			elif i == '(':
				self.push(i)

			elif i == ')':
				while (not self.is_empty()) and (self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.is_empty()) and (self.peek() != '('):
					return -1
				else:
					self.pop()
			else:
				while (not self.is_empty()) and self.not_greater(i):
					self.output.append(self.pop())
				self.push(i)

		while not self.is_empty():
			self.output.append(self.pop())

		print(''.join(self.output))


exp = "a+b*(c^d-e)^(f+g*h)-i"
conversion_obj = Conversion()
conversion_obj.infix_to_postfix(exp)


