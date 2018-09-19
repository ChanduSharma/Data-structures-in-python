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

	def postfix_to_prefix(self, expression):

		for i in expression:

			if not self.is_operand(i):

				a = self.pop()
				b = self.pop()

				self.push(i + b + a)
			else:
				self.push(i)

		print(self.pop())

exp = "ABC/-AK/L-*"
conversion_obj = Conversion()

conversion_obj.postfix_to_prefix(exp)


