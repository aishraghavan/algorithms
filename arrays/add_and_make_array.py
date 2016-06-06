"""
https://www.careercup.com/question?id=5696736490160128

consider an array1={1,1,1,1,1,1,1,1,1,1}
if n=4 add first four elements and next four elements
result : array1={4,4,2}
if n=3 add first three elements and next three elements repeat process untill size of array <=n
result1:
array1={3,3,3,1}
result2 : array1={6,4}
"""

def add_and_make_array(input, size):
    if (len(input) == 0) or (size == 0):
        return None
    output = []
    start = 0
    sum = 0
    start_size = 0
    while start<len(input):
        start_size += 1
        sum += input[start]
        #print "start_size: {0}, size :{1}, sum: {2}, output:{3}".format(start_size, size, sum, output)
        if start_size == size:
            output.append(sum)
            sum = 0
            start_size = 0
        start +=1
    if sum != 0:
        output.append(sum)
    return output

def add_and_make_array_less_variables(input, size):
    if (len(input) == 0) or (size == 0):
        return None
    output = []
    start = 0
    sum = 0
    while start<len(input):
        for index in range(start, start+size):
            if index < len(input):
                sum += input[index]
        output.append(sum)
        start = start+size
        sum = 0
    return output

array1=[1,1,1,1,1,1,1,1,1,1]
print "size: {0} add_and_make_array returns:{1} and better sol:{2}".format(4, add_and_make_array(array1, 4), add_and_make_array_less_variables(array1, 4))
print "size: {0} add_and_make_array returns:{1} and better sol:{2}".format(3, add_and_make_array(array1, 3), add_and_make_array_less_variables(array1, 3))
print "size: {0} add_and_make_array returns:{1} and better sol:{2}".format(5, add_and_make_array(array1, 5), add_and_make_array_less_variables(array1, 5))
print "size: {0} add_and_make_array returns:{1} and better sol:{2}".format(0, add_and_make_array(array1, 0), add_and_make_array_less_variables(array1, 0))
print "size: {0} add_and_make_array returns:{1} and better sol:{2}".format(4, add_and_make_array([], 4), add_and_make_array_less_variables([], 4))
