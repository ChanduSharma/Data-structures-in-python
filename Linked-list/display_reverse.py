#!/usr/bin/env python3

# Function to display reverse of a linked list.

class Node:
	def __init__(self, val, node):
		self.data = val
		self.next_node = node

def display_reverse(head):

	if not head:
		return None

	display_reverse(head.next_node)
	print(head.data)

