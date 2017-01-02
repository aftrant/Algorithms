def InsertionSort(A, n):
	for j in range(1,n):
		key = A[j]
		i = j - 1
		while A[i] > key and i >= 0:
			A[i + 1] = A[i]
			i -= 1
		A[i + 1] = key
	return A

print InsertionSort([6, 2, 7, 1, 13, 4], 6)

def InsertionSortNoN(A):
	for i in range(1, len(A)):
		key = A[i]
		k = i
		while k > 0 and key < A[k - 1]:
			A[k] = A[k - 1]
			k -= 1
		A[k] = key
	return A

print InsertionSortNoN([6, 2, 7, 1, 13, 4])
