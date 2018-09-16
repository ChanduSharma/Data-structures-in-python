#!/usr/bin/env python3
# Finding the nth node from end using brute force method
# space complexity O(1)
# Time complexity O(n^2)



class Node:

	def __init__(self, val, node):
		self.data = val
		self.next_node = node


def insert_beg(head, val):

	return Node(val, head)

def count_element(head):

	count = 0
	while head:
		count += 1
		head = head.next_node
	return count

def search_list(head, n):

	temp = head
	while temp:

		if count_element(temp) < n:
			return "element out of bound"

		if count_element(temp) == n:
			return temp.data
		temp = temp.next_node


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
	print('Searching 8rd node from end')

	print(search_list(x, 8))

