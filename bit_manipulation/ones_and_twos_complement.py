"""
http://www.geeksforgeeks.org/1s-2s-complement-binary-number/
"""

def get_ones_complement(string):
    if not string:
        return None
    ones_comp = ""
    for element in string:
        i_ele = int(element)
        ones_comp += str(i_ele ^1)
    return ones_comp

def get_twos_complement(string):
    if not string:
        return None
    ones_comp = get_ones_complement(string)
    twos_complement = int(ones_comp) + 1
    binary = bin(twos_complement)[2:]
    print "twos complement of {0} is {1}".format(string, binary)


print "ones complement of {0} is {1}".format('1100', get_ones_complement('1100'))
print "ones complement of {0} is {1}".format('0111', get_ones_complement('0111'))
get_twos_complement('1100')
get_twos_complement('0111')
