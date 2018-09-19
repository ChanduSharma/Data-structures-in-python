# Function to reverse the stack using push and pop operations

import random

class myStack:

	def __init__(self):

		self.array = []

	def is_empty(self):
		return self.array == []

	def push(self, val):

		self.array.append(val)

	def pop(self):

		if not self.is_empty():
			return self.array.pop()

	
def insert_at_bottom(my_stack, val):
		if my_stack.is_empty():
			my_stack.push(val)
		else:
			temp = my_stack.pop()
			insert_at_bottom(my_stack, val)
			my_stack.push(temp)


def reverse_stack(my_stack):
		if not my_stack.is_empty():
			data = my_stack.pop()
			reverse_stack(my_stack)
			insert_at_bottom(my_stack, data)


my_stack = myStack()
for i in range(10):
	my_stack.push(random.randint(1,100))

# Not a right way but stack ADT doesnot have a method to print all elements
# inside it and poping all will require creating new stack to push those.
print(*my_stack.array)
reverse_stack(my_stack)
print(*my_stack.array)

