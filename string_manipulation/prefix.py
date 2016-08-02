def prefix_array(array):
	lsp = [0]*len(array)
	j = 0
	i = 1
	while i<len(array):
		if array[i] == array[j]:
			lsp[i] = j+1
			i += 1
			j += 1
		else:
			if j == 0:
				lsp[i] = 0
				i += 1
			else:
				while(j>0):
					j = lsp[j-1]
	return lsp

if __name__ == "__main__":
	array = "abcabcde"
	print prefix_array(array)
	array = "abcabcd"
	print prefix_array(array)
	array = "abababc"
	print prefix_array(array)
