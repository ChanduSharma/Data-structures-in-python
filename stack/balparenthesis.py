#!/usr/bin/env python3

# Stack as an abstract Data Type

class MyStack:

	def __init__(self):
		self.mylist = list()

	def push(self, val):

		self.mylist.append(val)

	def pop(self):

		if self.mylist:
			return self.mylist.pop()
		else:
			raise StackEmptyException('Stack is Empty.')

	def top(self):
		return self.mylist[-1]

	def stack_size(self):
		return len(self.mylist)

	def is_empty_stack(self):
		return self.mylist == []

if __name__ == '__main__':
	
	my_stack = MyStack()

	driver_symbol = "[()[({}{})]]"

	for symbol in driver_symbol:
		
		if symbol in ('(','{','['):
			my_stack.push(symbol)
			continue

		if my_stack.is_empty_stack():
			break

		if symbol in (']','}',')'):
			if symbol == ')':
				if my_stack.top() != '(':
					break
				else:
					my_stack.pop()
			elif symbol == '}':
				if my_stack.top() != '{':
					break
				else:
					my_stack.pop()
			elif symbol == ']':
				if my_stack.top() != '[':
					break
				else:
					my_stack.pop()


	if not my_stack.is_empty_stack():
		print('Stack unbalanced.')
	else:
		print('Stack balanced.')




