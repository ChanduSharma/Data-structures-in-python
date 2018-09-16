#!/usr/bin/env python3

class Node:

	def __init__(self, val, node):
		self.data = val
		self.next = node


def insert_at_beg(head, val):

	return Node(val,head)


def display_list(linked_list):

	while linked_list:
		print(linked_list.data)
		linked_list = linked_list.next

if __name__ == '__main__':
	
	x = Node(3, None)
	x.next = Node(8, None)
	x.next.next = Node(4, None)
	x.next.next.next = Node(5, None)

	display_list(x)
	x = insert_at_beg(x, 12)
	print('Display list')
	display_list(x)
