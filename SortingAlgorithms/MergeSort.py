def mergeSort(L):
	
	n = len(L)
	# base case
	if (n <= 1):
		return L
	
	L1 = L[:n//2]
	L2 = L[n//2:]

	mergeSort(L1)
	mergeSort(L2)

	return merge(L, L1, L2)


def merge(L, L1, L2):

	i = 0
	j = 0
	k = 0

	while (j < len(L1)) or (k < len(L2)):
		if (j < len(L1)):
			if (k < len(L2)):
				if (L1[j] < L2[k]):
					L[i] = L1[j]
					j += 1
				else:
					L[i] = L2[k]
					k += 1
			else:
				L[i] = L1[j]
				j += 1
		else:
			L[i] = L2[k]
			k += 1

		i += 1
	
	return L


print mergeSort([3,7,12,8,3,6,7,2])
