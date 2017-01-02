def quickSort(L):
	
	n = len(L)
	if (n <= 1):  # base case
		return L

	pivot = L[0]

	L1 = []
	L2 = []

	for i in L[1:]:
		if (i < pivot):
			L1.append(i)
		else:
			L2.append(i)


	quickSort(L1)
	quickSort(L2)

	# join
	L[:] = []

	for element in L1:
		L.append(element)
	L.append(pivot)
	for element in L2:
		L.append(element)

	return L

print quickSort([3, 6, 8, 2, 4, 9])
