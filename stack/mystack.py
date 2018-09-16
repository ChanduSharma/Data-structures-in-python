#!/usr/bin/env python3

# Stack as an abstract Data Type

class MyStack:

	def __init__(self):
		self._mylist = list()

	def push(self, val):

		self._mylist.append(val)

	def pop(self):

		if self._mylist:
			return self._mylist.pop(0)
		else:
			raise StackEmptyException('Stack is Empty.')

	def top(self):
		return self._mylist[0]

	def stack_size(self):
		return len(self._mylist)

	def is_empty_stack(self):
		return self._mylist == []


if __name__ == '__main__':
	
	my_stack = MyStack()
	my_stack.push(2)
	my_stack.push(34)
	my_stack.push(22)
	my_stack.push(21)
	my_stack.push(12)

	print(my_stack.top())
	my_stack.pop()
	print(my_stack.top())
