#http://www.geeksforgeeks.org/searching-for-patterns-set-1-naive-pattern-searching/
"""
Algorithm analysis: O(nm) general terms

n = len(txt)
m = len(pat)

Best case: O(len(pat)) ==> O(n)
Worst case: O(len(pat)*(len(txt)-len(pat)+1)) ==> O(m*(n-m+1))

Better algorithm : http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
"""
# Python program for Naive Pattern Searching
def search(pat, txt):
	if pat == None or txt == None:
		return None
	if len(pat) > len(txt):
		return None
	for i in range(len(txt)-len(pat)):  # first loop
		temp = txt[i:i+len(pat)]		# second loop
		if temp == pat:
			print "found at index : {0}".format(i)
	return -1


print "search({0}, {1})".format("hello", "hello there hello party")
search("hello", "hello there hello party")
print "search({0}, {1})".format("llo", "hello there hello party")
search("llo", "hello there hello party")
print "search({0}, {1})".format("AABA", "AABAACAADAABAAABAA")
search("AABA", "AABAACAADAABAAABAA")
print "best case: search({0}, {1}) not found".format("FAA","AABCCAADDEE")
search("FAA","AABCCAADDEE")
print "worst case: search({0}, {1})".format("AAAAA", "AAAAAAAAAAAAAAAAAA")
search("AAAAA", "AAAAAAAAAAAAAAAAAA")
print "worst case: search({0}, {1})".format("AAAAB", "AAAAAAAAAAAAAAAAAB")
search("AAAAB", "AAAAAAAAAAAAAAAAAB")

