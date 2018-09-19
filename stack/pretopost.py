# Postfix evaluation

class Conversion:

	def __init__(self):
		self.array = []

	def is_empty(self):
		return self.array == []

	def push(self, val):
		self.array.append(val)

	def is_operand(self, ch):
		return ch.isalpha()

	def pop(self):

		if not self.is_empty():
			return self.array.pop()
		else:
			return '$'

	def prefix_to_postfix(self, expression):

		for i in expression[::-1]:

			if not self.is_operand(i):

				a = self.pop()
				b = self.pop()

				self.push(a + b + i)
			else:
				self.push(i)

		print(self.pop())

exp = "*-A/BC-/AKL"
conversion_obj = Conversion()

conversion_obj.prefix_to_postfix(exp)


