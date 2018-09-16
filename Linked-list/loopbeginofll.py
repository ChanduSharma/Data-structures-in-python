#!/usr/bin/env python3

# Function to find starting node of loop 
# in linked list.

# Space Complexity: O(1)
# Time Complexity: O(n)

# class Node:
# 	"""
# 		Class to define a node in a linked list.
# 	"""
# 	def __init__(self, val, node):
# 		self.data = val
# 		self.next_node = node



def find_begin_of_loop(head):

	slow_pointer = head
	fast_pointer = head
	loop_exists = 0

	while slow_pointer and fast_pointer and fast_pointer.next:
		
		slow_pointer = slow_pointer.next_node
		fast_pointer = fast_pointer.next_node.next_node

		if slow_pointer == fast_pointer:
			loop_exists = 1
			break

	if loop_exists:
		slow_pointer = head

		while slow_pointer != fast_pointer:
			slow_pointer = slow_pointer.next_node
			fast_pointer = fast_pointer.next_node

		return slow_pointer
	return None
