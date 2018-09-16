 #!/usr/bin/env python3

 # Function to merge two linked list.

class Node:
	def __init__(self, val, node):
		self.data = val
		self.next_node = node


def merge_list(a, b):

	if not a:
		return b

	if not b:
		return a

	if a.data <= b.data:
		result = a
		result.next_node = merge_list(a.next_node, b)
	else:
		result = b
		result.next_node = merge_list(a, b.next_node)

	return result
