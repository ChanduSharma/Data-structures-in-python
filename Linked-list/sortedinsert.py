#!/usr/bin/env python3

# Function to insert a node in a sorted list

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
def sorted_insert(head, val):

	temp = head
	temp2 = head
	if not head:
		return insert_at_beg(head, val)

	while temp and temp.data < val:
		temp2 = temp
		temp = temp.next_node

	new_node = Node(val, temp)
	temp2.next_node = new_node
	return head



if __name__ == '__main__':
	x = None
	x = insert_at_beg(x, 9)
	x = insert_at_beg(x, 7)
	x = insert_at_beg(x, 5)
	x = insert_at_beg(x, 2)
	x = insert_at_beg(x, 1)

	print_list(x)
	print()

	x = sorted_insert(x, 3)
	print_list(x)