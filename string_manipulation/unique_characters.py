"""
Unique characters
"""
def unique_characters(str):
    hashmap = {}
    for ele in str:
        if ele in hashmap.keys():
            return False
        else:
            hashmap[ele]=True
    return True

"""
#other ideas
1. Boolean array
2. Boolean variable
3. If we restrict to 256 ASCII, we can check for length of array greater than 256 and fail itself.
"""

if __name__ == "__main__":
    print unique_characters("abcd")
    print unique_characters("abca")
