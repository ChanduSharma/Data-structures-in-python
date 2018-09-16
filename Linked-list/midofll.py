#!/usr/bin/env python3

# Functions to find  middle of a linked list.

class Node:

	def __init__(self, val, node):
		self.data = val
		self.next_node = node


def mid_of_ll(head):

	slow_pointer = head
	fast_pointer = head
	
	i = 0

	while slow_pointer.next_node:

		if i == 0:
			fast_pointer = fast_pointer.next_node
			i = 1
		elif i == 1:
			slow_pointer = slow_pointer.next_node
			fast_pointer = fast_pointer.next_node
			i = 0

	return slow_pointer