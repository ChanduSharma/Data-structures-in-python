#!/usr/bin/env python3

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

def insert_at_end(head, val):

	new_node = Node(val, None)

	if not head:
		new_node.next_node = new_node
		return new_node
	else:
		
		temp = head
		while True:

			if temp.next_node == head:
				break
			temp = temp.next_node

		temp.next_node = new_node
		new_node.next_node = head
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

	x = insert_at_end(x, 21)
	x = insert_at_end(x, 12)
	x = insert_at_end(x, 65)
	print_list(x)
	print()