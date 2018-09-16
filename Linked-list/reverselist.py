#!/usr/bin/env python3

# Funtion to reverse a linked list
# Space complexity : O(1)
# Time complexity : O(n)

class Node:

	def __init__(self, val, node):
		self.data = val
		self.next_node = node


def insert_at_beg(head, val):
	return Node(val, head)

def print_list(head):

	while head:
		print(head.data)
		head = head.next_node


def reverse_list(head):

	new_node = None
	temp = None

	while head:
		new_node = head.next_node

		head.next_node = temp

		temp = head

		head = new_node

	return temp

if __name__ == '__main__':
	x = None
	x = insert_at_beg(x, 23)
	x = insert_at_beg(x, 2)
	x = insert_at_beg(x, 43)
	x = insert_at_beg(x, 9)
	x = insert_at_beg(x, 10)

	print_list(x)
	print()

	x = reverse_list(x)
	print_list(x)