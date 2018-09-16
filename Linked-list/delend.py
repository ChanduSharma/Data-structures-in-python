#!/usr/bin/env python
# -*- coding: utf-8 -*-
  

class Node:
	def __init__(self, val, node):
		self.data = val
		self.next_node = node
		
def del_at_end(head):
	if not head or not head.next_node:
		return None
	else:
		temp = head
		while temp.next_node.next_node:
			temp = temp.next_node
			
		temp.next_node = None
		return head
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
	x = del_at_end(x)
	print('Display list')
	display_list(x)
