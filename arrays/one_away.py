"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false Hints:#23, #97, #130
"""

def one_away(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    len_diff = abs(len_str1- len_str2)
    import ipdb; ipdb.set_trace()
    #length difference cannot be more than 1
    if len_diff >1:
        return False
    count = 0
    i = j = 0
    while i<len_str1 and j<len_str2:
        if str1[i]!= str2[j]:
            count += 1
        i += 1
        j += 1
    import ipdb; ipdb.set_trace()
    #if i+1=len_str1 and j:

    #if j+1=len_str2:

    if count == 0 or count ==1:
        return True
    return False

def format_and_print(array, output):
    print "Calling one_away with : {0} and {1}".format(array[0], array[1])
    result = one_away(array[0], array[1])
    print result

if __name__ == "__main__":
    input_array = [
                ("pale","ple"),
                ("pales","pale"),
                ("pale","bale"),
                ("pale","bake")
                ]
    output_array = [True, True, True, False]
    format_and_print(("pale","ple"), True)
