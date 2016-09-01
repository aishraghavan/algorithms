"""
https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
"""

def min_coins_to_make_denomination(sum, coin_array):
	#Initialize to -1
	denomination_table = [-1]*(sum+1)
	denomination_table[0] = 0
	for index in range(1, sum+1):
		print "sum :", index
		min_calculation = sum
		curr_calculation = 0
		for val_index in range(len(coin_array)):
			if coin_array[val_index]<=index:
				#print "considered for value", coin_array[val_index]
				#print "balance", index-coin_array[val_index]
				curr_calculation = denomination_table[index-coin_array[val_index]]+1
				if curr_calculation<min_calculation:
					min_calculation = curr_calculation
		print "min coins needed", min_calculation
		denomination_table[index] = min_calculation
		print "---------"
	return denomination_table

def min_coins_to_make_denomination_list(sum, coin_array):
	#Initialize to -1
	denomination_table = [-1]*(sum+1)
	denomination_table[0] = 0

	# denomination_coins_table = [[]]*(sum+1)
	# print denomination_coins_table
	# denomination_coins_table[0] = [0]
	for index in range(1, sum+1):
		print "sum :", index
		min_calculation = sum
		curr_calculation = 0
		#temp_list = []
		for val_index in range(len(coin_array)):
			if coin_array[val_index]<=index:
				print "considered for value", coin_array[val_index]
				#print "balance", index-coin_array[val_index]
				curr_calculation = denomination_table[index-coin_array[val_index]]+1
				if curr_calculation<min_calculation:
					#temp_list.append(coin_array[val_index])
					min_calculation = curr_calculation
		print "min coins needed", min_calculation
		denomination_table[index] = min_calculation
		#denomination_coins_table[index] = temp_list
		print "---------"
	#print denomination_coins_table
	return denomination_table



if __name__ == "__main__":
	print "Calling min_coins_to_make_denomination(11, [1,3,5])", min_coins_to_make_denomination(11, [1,3,5])
	print "Calling min_coins_to_make_denomination_list(11, [1,3,5])", min_coins_to_make_denomination_list(11, [1,3,5])