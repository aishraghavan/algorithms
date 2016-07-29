def power_set(input_array):
	power_set_list = []
	total_count = pow(2, len(input_array))

	for counter in range(total_count):
		local_list = []
		for j in range(len(input_array)):
			if counter&(1<<j):
				local_list.append(input_array[j])
		power_set_list.append(local_list)
	return power_set_list

if __name__ == "__main__":
	input_array = [1,2,3]
	print power_set(input_array)

	
