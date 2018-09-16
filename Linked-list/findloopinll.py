#!/usr/bin/env python3

# Funtion to find the cycle in the linked list.
# Based on the Floyd cycle finding algorithm.

# Space Complexity: O(1)
# Time Complexity: O(n)

# class Node:
# 	'''
# 		Class defining the node of the linked list
# 	'''
# 	def __init__(self, val, node):
# 		self.data = val
# 		self.next_node = node

def is_loop_exists(head):

	slow_pointer = head
	fast_pointer = head

	while slow_pointer and fast_pointer and fast_pointer.next:
		
		slow_pointer = slow_pointer.next_node
		fast_pointer = fast_pointer.next_node.next_node

		if slow_pointer == fast_pointer:
			return 1

	return 0