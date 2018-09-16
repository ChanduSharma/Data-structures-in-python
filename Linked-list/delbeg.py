#!/usr/bin/env python
# -*- coding: utf-8 -*-
  

class Node:
	def __init__(self, val, node):
		self.data = val
		self.next_node = node
		
def del_at_beg(head):
	return head.next_node
	
def display_list(head):
	
	while head:
		print(head.data)
		head = head.next_node
	

if __name__ == '__main__':
	
	x = Node(3, None)
	x.next_node = Node(8, None)
	x.next_node.next_node = Node(4, None)
	x.next_node.next_node.next_node = Node(5, None)

	display_list(x)
	x = del_at_beg(x)
	print('Display list')
	display_list(x)
