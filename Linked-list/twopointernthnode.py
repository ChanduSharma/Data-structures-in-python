#!/usr/bin/env python3
# Finding the nth node from end using two pointer method
# space complexity O(1)
# Time complexity O(n)



class Node:

	def __init__(self, val, node):
		self.data = val
		self.next_node = node


def insert_beg(head, val):

	return Node(val, head)


def search_list(head, n):

	temp = head
	temp2 = None

	for i in range(1, n):
		if temp:
			temp = temp.next_node

	while temp:

		if not temp2:
			temp2 = head
		else:
			temp2 = temp2.next_node
		temp = temp.next_node

	if temp2:
		return temp2.data
	else:
		return 'Out of bounds.'
	
			

def print_list(head):

	while head:
		print(head.data)
		head = head.next_node


if __name__ == '__main__':
	
	x = None
	x = insert_beg(x, 32)
	x = insert_beg(x, 12)
	x = insert_beg(x, 35)
	x = insert_beg(x, 1)
	x = insert_beg(x, 3)
	x = insert_beg(x, 21)

	print_list(x)
	print('Searching 3rd node from end')

	print(search_list(x, 1))

