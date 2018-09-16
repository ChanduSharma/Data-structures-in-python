#!/usr/bin/env python3

# Function to find common point of two linked list.

# class Node:
# 	def __init__(self, val, node):
# 		self.data = val
# 		self.next_node = node

def count_element(head):

	count = 0
	while head:
		count += 1
		head = head.next_node

	return count

def common_point(head1, head2):

	count1 = count_element(head1)
	count2 = count_element(head2)

	to_move = 0
	if count1 > count2:
		to_move = count1 - count2
		for i in range(to_move):
			head1 = head1.next_node

	else:
		to_move = count2 - count1
		for i in range(to_move):
			head2 = head2.next_node


	while head1 != head2:
		head1 = head1.next_node
		head2 = head2.next_node

	return head1


