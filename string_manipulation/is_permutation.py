"""
Is Permutation characters

1. have two hashmaps and compare the hashmaps at once.
2. one hashmap with increment for one string and decrement for other.
3. sort the strings and compare

"""
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    hashmap = {}
    for ele in str1:
        if ele in hashmap.keys():
            hashmap[ele] = hashmap[ele] + 1
        else:
            hashmap[ele] = 1
    for ele in str2:
        if ele in hashmap.keys():
            hashmap[ele] = hashmap[ele] - 1
            if hashmap[ele]< 0:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    print is_permutation("abcd", "dcab")
    print is_permutation("abca", "bbbb")
