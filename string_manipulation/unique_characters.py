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

if __name__ == "__main__":
    print unique_characters("abcd")
    print unique_characters("abca")
