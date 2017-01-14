def BinarySearch(A, x):
	end = len(A) - 1
	start = 0

	while start <= end:
		mid = (start + end)/2
		if A[mid] == x:
			return mid
		elif x < A[mid]:
			end = mid - 1
		else:
			start = mid + 1
	return -1  # did not found x in array A
