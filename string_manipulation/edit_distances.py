"""
http://www.geeksforgeeks.org/check-if-two-given-strings-are-at-edit-distance-one/

Input:  s1 = "geeks", s2 = "geek"
Output: yes
Number of edits is 1

Input:  s1 = "geeks", s2 = "geeks"
Output: no
Number of edits is 0

Input:  s1 = "geaks", s2 = "geeks"
Output: yes
Number of edits is 1

Input:  s1 = "peaks", s2 = "geeks"
Output: no
Number of edits is 2
"""
class InputError(Exception):
    def __init__(self, message):
        self.message = message

def _error_checking(string1, string2):
    if not string1 or not string2:
        raise InputError("Empty string")
    return


def edit_distances(string1, string2):
    _error_checking(string1, string2)
    if string1 == string2:
        return False
    if len(string1) != len(string2):
        return False
    resultant_input = zip(list(string1), list(string2))
    count_edits = 0
    for char_1,char_2 in resultant_input:
        if char_1 != char_2:
            count_edits += 1
        if count_edits >1:
            return False
    if count_edits == 1:
        return True
    return False


print "check edit_distances for {0} and {1} : {2}".format("geeks", "geek", edit_distances("geeks", "geek"))
print "check edit_distances for {0} and {1} : {2}".format("geeks", "geeks", edit_distances("geeks", "geeks"))
print "check edit_distances for {0} and {1} : {2}".format("geaks", "geeks", edit_distances("geaks", "geeks"))
print "check edit_distances for {0} and {1} : {2}".format("peaks", "geeks", edit_distances("peaks", "geeks"))
