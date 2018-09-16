#!/usr/bin/env python3

import gc

class Node:

	def __init__(self, val, node):
		self.data = val
		self.next_node = node


# Function to print circular linked list.
def print_list(head):

	temp = head

	if head:
		while True:

			print(temp.data)
			temp = temp.next_node

			if temp == head:
				break


def insert_at_beg(head, val):

	new_node = Node(val, None)
	
	if not head:
		new_node.next_node = new_node
	else:
		new_node.next_node = head
		temp = head
		while True:

			if temp.next_node == head:
				break
			temp = temp.next_node

		temp.next_node = new_node

	return new_node

# Funtion to delete at the beginning of the linked list.
def del_at_beg(head):

	temp = head

	if not head:
		return None

	while temp.next_node != head:
		temp = temp.next_node

	temp.next_node = head.next_node
	gc.collect()
	return head.next_node

def del_at_end(head):

	if not head:
		return None
	else:
		temp = head
		temp2 = head
		while temp.next_node != head:
			temp2 = temp
			temp = temp.next_node

		temp2.next_node = head
		gc.collect()
		return head



if __name__ == '__main__':
	x = None
	x = insert_at_beg(x, 3)
	x = insert_at_beg(x, 4)
	x = insert_at_beg(x, 6)
	x = insert_at_beg(x, 7)
	x = insert_at_beg(x, 34)

	print_list(x)
	print()

	x = del_at_beg(x)
	print_list(x)
	print()
	x = del_at_end(x)
	print_list(x)
	print()
