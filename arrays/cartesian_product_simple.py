def cartesian_product_simple(arr1, arr2):
	if not arr1 or not arr2:
		return
	prod_c= []
	for ele1 in arr1:
		#temp  = []
		for ele2 in arr2:
			prod_c.append([ele1, ele2])
		

	return prod_c


# def cartesian_product_complex(array, n):
# 	for big_ind in range(len(array)):
# 		for inner_ind in range(len(array[big_ind])):


arr1 = [1,2,3]
arr2 = ['a','b']
arr3 = ['p','q']
result = cartesian_product_simple(arr1, arr2)
print cartesian_product_simple(result, arr3)
#print [(a, b, c) for a in [1,2,3] for b in ['a','b'] for c in [4,5]]
print [(a,b,c) for a in arr1 for b in arr2 for c in arr3]

def cartesian (lists):
    if lists == []: return [()]
    return [x + (y,) for x in cartesian(lists[:-1]) for y in lists[-1]]

print cartesian([[1, 2, 3], [2, 4, 6], [3, 6, 9]])