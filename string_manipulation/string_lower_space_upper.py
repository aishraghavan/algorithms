"""
https://www.careercup.com/question?id=5647284379320320

amazon-interview-questions0
A string contains a-z, A-Z and spaces. Sort the string so that all lower cases
are at the beginning, spaces in the middle and upper cases at the end. Original
order among lower and upper cases needs to remain the same. For example:
a cBd LkmY becomes ackm BLY. Is there a way in O(n) without extra space?
"""

def lower_space_upper_simple(input):
    if not input or len(input)==0 or input=="":
        return None
    output_str = ''
    #small letters
    for ele in input:
        if (ord(ele)>=97 and ord(ele)<=122):
            output_str += ele
    #space
    for ele in input:
        if (ord(ele)==32):
            output_str += ele
    #Big letters
    for ele in input:
        if (ord(ele)>=65 and ord(ele)<=90):
            output_str += ele
    return output_str

print "string: {0} and lower_space_upper_simple() is :{1}".format("a cBd LkmY", lower_space_upper_simple("a cBd LkmY"))
print "string: {0} and lower_space_upper_simple() is :{1}".format("", lower_space_upper_simple(""))
print "string: {0} and lower_space_upper_simple() is :{1}".format(None, lower_space_upper_simple(None))
