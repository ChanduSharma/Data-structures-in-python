#!/usr/bin/env python3

def binary(A, n):
	if n < 1:
		print(''.join(A))
	else:
		A[n - 1] = '0'
		binary(A, n - 1)
		A[n - 1] = '1'
		binary(A, n - 1)


if __name__ == '__main__':
	print('Enter the length of binary string.')
	try:
		n = int(input())
		A = [0 for i in range(n)]

		binary(A, n)
	except ValueError:
		print("Length of string should be integer")