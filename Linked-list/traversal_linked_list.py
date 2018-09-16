#! /usr/bin/env python3


class Node:

	def __init__(self, data, node):
		self.data = data
		self.next = node


def list_length(ll):

	count = 0
	while ll is not None:
		count += 1
		ll = ll.next

	return count


if __name__ == '__main__':

	 x = Node(3, None)
	 x.next = Node(8, None)
	 x.next.next = Node(4, None)
	 x.next.next.next = Node(5, None)

	 print(list_length(x))