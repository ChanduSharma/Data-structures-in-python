#!/usr/bin/env python3

def tower_of_hanoi(n, source, to, aux):

	# If the number of disk is one just move it from source to destination
	if n == 1:
		print('Move disk 1 from {} tower to {} tower'.format(source, to))
	else:

		tower_of_hanoi(n-1, source , aux, to)

		print('Move the {} disk from {} tower to {} tower'.format(n,source, to))

		tower_of_hanoi(n-1, aux, to, source)


if __name__ == '__main__':
	print('Enter the number of disk')

	try:
		number_of_disk = int(input())
		source = 'source'
		destination = 'destination'
		aux = 'auxiliary'
		tower_of_hanoi(number_of_disk, source, destination, aux)
	except ValueError:
		print('Enter a number')
