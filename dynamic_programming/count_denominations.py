"""
count_denominations

coin_exchange()

http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
"""

def coin_exchange(coin_array, size, amount):
	#print "Calling coin_exchange with coin_array:{0} size:{1} amount:{2}".format(coin_array, size, amount)
	# if amount is 0
	if amount == 0:
		return 1

	# if amount<0
	if amount <0:
		return 0

	#if amount to be sorted exists and greater than 1 but coin size is 0 or less
	if amount>=1 and size<=0:
		return 0

	return(coin_exchange(coin_array, size-1, amount)
		+
		#amount - last value in the array
		coin_exchange(coin_array, size, amount-coin_array[size-1]))


# def coin_exchange_with_table(coin_array, size, amount):
# not completed
# 	table = [[0]*amount]*size
# 	print table
# 	print coin_exchange_improved(coin_array, size, amount, table)
# 	print table


# def coin_exchange_improved(coin_array, size, amount, table):
# 	print "Calling coin_exchange with coin_array:{0} size:{1} amount:{2} table: {3}".format(coin_array, size, amount, table)
# 	# if amount is 0
# 	if amount == 0:
# 		table[size-1][amount-1] = 1
# 		return 1

# 	# if amount<0
# 	if amount <0:
# 		table[size-1][amount-1] = 0
# 		return 0

# 	#if amount to be sorted exists and greater than 1 but coin size is 0 or less
# 	if amount>=1 and size<=0:
# 		table[size-1][amount-1] = 0
# 		return 0

# 	return(coin_exchange_improved(coin_array, size-1, amount, table)
# 		+
# 		#amount - last value in the array
# 		coin_exchange_improved(coin_array, size, amount-coin_array[size-1], table))

def format_and_print(coin_array, amount):
	print "-------------"
	print "Input coin_array: {0} and amount: {1}".format(coin_array, amount)
	print coin_exchange(coin_array, len(coin_array), amount)
	#coin_exchange_with_table(coin_array, len(coin_array), amount)
	print "-------------"

if __name__ == "__main__":
	# coin_array = [1,2,3]
	# amount = 5
	# format_and_print(coin_array, amount)
	#format_and_print([1,2], 3)
	format_and_print([1,2,3], 4)
	

