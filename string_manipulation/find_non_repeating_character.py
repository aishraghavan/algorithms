"""
http://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/
"""
def find_non_repeating_character_navie(string):
	i = 0
	j = 0
	count = 1
	while i< len(string):
		j = i+1
		while j< len(string):
			if string[i] == string[j]:
				count += 1
			j+=1
		if count == 1:
			return string[i] 
		i +=1
		count = 1


def find_non_repeating_character(string):
	hash_map = {}
	for ele in string:
		if ele in hash_map.keys():
			hash_map[ele] += 1
		else:
			hash_map[ele] = 1

	for key, ele in hash_map.items():
		if ele ==1:
			return	key


if __name__== "__main__":
	strings = ["geeksforgeeks", "geekhello"]
	for string in strings:
		print "Non repeating char in {0} is : {1} better sol: {2}".format(
			string, 
			find_non_repeating_character_navie(string),
			find_non_repeating_character(string))