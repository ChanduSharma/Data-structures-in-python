#!/usr/bin/env python3

class Node:

	def __init__(self, val, left, right):
		self.data = val
		self.left = left
		self.right = right


def insert_at_beg(head, val):

	new_node = Node(val, None, head)

	if head:
		head.left = new_node
	
	return new_node

def insert_at_end(head, val):

	new_node = Node(val, None, None)
	if not head:
		return new_node

	temp = head
	while temp.right:
		temp = temp.right

	temp.right = new_node
	new_node.left = temp

	return head

def insert_at_pos(head, val, pos):

	new_node = Node(val, None, None)

	if pos == 1:

		new_node.right = head

		if head:
			head.left = new_node
		return new_node

	temp = head
	k = 1

	while k < pos - 1 and temp.right:
		temp = temp.right
		k += 1

	new_node.right = temp.right
	new_node.left = temp

	if temp.right:
		temp.right.left = new_node

	temp.right = new_node

	return head


def print_list(head):

	while head:
		print(head.data)
		head = head.right


if __name__ == '__main__':
	x = None
	x = insert_at_beg(x, 3)
	x = insert_at_beg(x, 5)
	x = insert_at_beg(x, 7)
	x = insert_at_beg(x, 9)
	print_list(x)
	print()
	x = insert_at_end(x, 9)
	x = insert_at_end(x, 10)
	x = insert_at_end(x, 14)
	print_list(x)
	print()

	x = insert_at_pos(x, 32, 1)
	
	x = insert_at_pos(x, 21, 2)
	x = insert_at_pos(x, 42, 3)
	x = insert_at_pos(x, 32, 5)
	print_list(x)



