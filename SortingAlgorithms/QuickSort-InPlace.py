def Partition(A, p, q):
	pivot = A[p]
	i = p
	for j in range(p + 1, q):
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[p], A[i] = A[i], A[p]
	return i

def QuickSort(A, p, q):
	if p < q:
		r = Partition(A, p, q)
		QuickSort(A, p, r-1)
		QuickSort(A, r+1, q)
	return A

print QuickSort([6, 10, 13, 5, 8, 3, 2, 11], 0, 8)
