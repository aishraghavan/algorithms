"""
http://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/

Input:  str1 = "aab", str2 = "xxy"
Output: True
'a' is mapped to 'x' and 'b' is mapped to 'y'.

Input:  str1 = "aab", str2 = "xyz"
Output: False
One occurrence of 'a' in str1 has 'x' in str2 and
other occurrence of 'a' has 'y'.
"""

def is_isomorphic(string1, string2):
    if not string1 or not string2:
        return
    if len(string1) != len(string2):
        return False
    input = zip(list(string1), list(string2))
    hash_map = {}
    for str1_index, str2_index in input:
        if not str1_index in hash_map.keys():
            hash_map[str1_index] = str2_index
        else:
            if hash_map[str1_index] != str2_index:
                return False
    return True

print "Check if {0} and {1} are isomorphic. Result: {2}".format("aab", "xxy", is_isomorphic("aab", "xxy"))
print "Check if {0} and {1} are isomorphic. Result: {2}".format("aab", "xyz", is_isomorphic("aab", "xyz"))
