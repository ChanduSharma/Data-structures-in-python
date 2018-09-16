#! /usr/bin/env python3

def k_string(A, n, k):

	if n < 1:
		print(''.join(list(map(str,A))))
	else:

		for i in range(k):
			# set the last value to value between 0...k-1
			A[n - 1] = i

			# recursive call to k_string for all cases.
			k_string(A, n - 1, k)


if __name__ == '__main__':
	print('Enter a the length of string.')
	try:
		n = int(input())
		k = int(input())
		A = [0 for i in range(n)]

		k_string(A, n, k)
	except ValueError:
		print('Enter only numbers')
