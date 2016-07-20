"""
https://leetcode.com/problems/valid-anagram/
"""
from sets import Set

def valid_anagram(str1, str2):
	# if not str1 or not str2:
	# 	return False
	if len(str1) != len(str2):
		return False
	for ele in str2:
		if ele not in str1:
			return False
	return True

def valid_anagram_sorted(str1, str2):
	if len(str1) != len(str2):
		return False
	str1 = sorted(str1)
	str2 = sorted(str2)
	if str1 ==  str2:
		return True
	return False

def valid_anagram_hash_map(str1, str2):
	if len(str1) != len(str2):
		return False
	hash_map = {}
	for ele in str1:
		if ele not in hash_map.keys():
			hash_map[ele] = 1
		else:
			hash_map[ele] += 1
	for ele in str2:
		if ele in hash_map.keys():
			hash_map[ele] -= 1
		else:
			return False
	if list(Set(hash_map.values())) == [0]:
		return True
	return False

def valid_anagram_set(str1, str2):
	if len(str1) != len(str2):
		return False
	set_a = Set(str1)
	set_b = Set(str2)
	if set_a == set_b:
		return True
	return False

def print_output(str1, str2):
	print "({0}, {1}) valid_anagram: {2} anagram_sorted:{3} valid_anagram_hash_map:{4} valid_anagram_set:{5}".format(str1, str2, 
		valid_anagram(str1, str2), 
		valid_anagram_sorted(str1, str2),
		valid_anagram_hash_map(str1, str2),
		valid_anagram_set(str1, str2))

if __name__ == "__main__":
	print_output("anagram", "nagaram")
	print_output("rat", "car")
	print_output("", "")
	print_output("aaca", "aacc")
