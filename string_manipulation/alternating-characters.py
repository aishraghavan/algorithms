"""
https://www.hackerrank.com/challenges/alternating-characters
### input####
4
aaaa
bbbbb
abababab
bababa

"""
import re

def test_alternating_characters():
    n = int(raw_input().strip())
    array_str = []
    for i in range(n):
        string = str(raw_input().strip())
        if len(string) != 0:
            array_str.append(string)

    for element in array_str:
        print alternating_characters(element)



def alternating_characters(string):
    string = string.upper()
    pattern = r'[^\.A-B]'
    if re.search(pattern, string) or string.isspace():
        return 0

    del_count = 0
    for index in range(0,len(string)-1):
        j_index= index +1
        if string[j_index] == string[index]:
            del_count += 1
    return del_count

if __name__ == "__main__":
    # print "aaaa", alternating_characters("aaaa")
    # print "bbbbb", alternating_characters("bbbbb")
    # print "abababab", alternating_characters("abababab")
    # print "bababa", alternating_characters("bababa")
    # print "aaabbb", alternating_characters("aaabbb")
    test_alternating_characters()
