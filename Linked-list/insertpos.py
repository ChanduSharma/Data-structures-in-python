#!/usr/bin/env python
# -*- coding: utf-8 -*-
  

class Node:
	def __init__(self, val, node):
		self.data = val
		self.next_node = node
		
def insert_at_pos(head, val, pos):
	
	if pos == 1:
		return Node(val, head)
		
	else:
		q = None
		k = 1
		temp = head
		
		while temp and k < pos:
			k += 1
			q = temp
			temp = temp.next_node
			
		q.next_node = Node(val, temp)
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
	x = insert_at_pos(x, 12, 3)
	print('Display list')
	display_list(x)
