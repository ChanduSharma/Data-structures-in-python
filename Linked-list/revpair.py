#!/usr/bin/env python3

# Function to reverse list in pairs.

class Node:

	def __init__(self, val, node):
		self.data = val
		self.next_node = node


def rev_pair(head):

	temp = None
	if not head and not head.next_node:

		return None

	else:

		temp = head.next_node
		head.next_node = temp.next_node
		temp.next_node = head
		head = temp

		head.next_node.next_node = rev_pair(head.next_node.next_node)

		return head