# sub routine to merge two sorted arrays
def merge_sorted_arrays(array1, array2):
	if len(array1) == 0 or len(array2) == 0:
		return
	i = j = 0 
	combined_array = []
	while (i< len(array1) and j< len(array2)):
		if array1[i] < array2[j]:
			combined_array.append(array1[i])
			i += 1
		else:
			combined_array.append(array2[j])
			j += 1

	while (i< len(array1)):
		combined_array.append(array1[i])
		i += 1

	while (j< len(array2)):
		combined_array.append(array2[j])
		j += 1
	return combined_array

# print merge_sorted_arrays([10,40,80], [20,90,100])
# print merge_sorted_arrays([100,140,180], [200,290,300])
# print merge_sorted_arrays([100,140,180], [20,90,105])


def merge_sort(list_of_numbers):
	if len(list_of_numbers) == 1:
		return list_of_numbers
	else:
		mid = len(list_of_numbers)/2
		L1_ = merge_sort(list_of_numbers[:mid])
		L2_ = merge_sort(list_of_numbers[mid:])
		return merge_sorted_arrays(L1_, L2_)

print merge_sort([1])
print merge_sort([11, 2])
print merge_sort([11, 20, 27, 4, 9])
print merge_sort([11, 20, 27, 4, 19])

