"""
http://www.geeksforgeeks.org/reorder-a-array-according-to-given-indexes/
"""

def reorder_array_according_to_given_indexes(array, index_array):
    if not array or not index_array:
        return 
    for i in range(len(array)):
        while(index_array[i]!=i):
            org_array_i = index_array[index_array[i]] #i
            org_array_element = array[index_array[i]]#array[i]
            print "step 1 org_array_i:{0}, org_array_element: {1}".format(org_array_i, org_array_element)

            #interchange
            array[index_array[i]] = array[i]
            index_array[index_array[i]] = index_array[i]

            #restore
            array[i] = org_array_element
            index_array[i] = org_array_i

    return array


def format_and_print(array, index_array, expected_output):
    print "Calling reorder_array_according_to_given_indexes  with input {0} and expected_output {1}".format(array, expected_output)
    print reorder_array_according_to_given_indexes(array, index_array)
    print "Result :{0}".format(array == expected_output)
    


if __name__ == "__main__":
    array  = [10, 11, 12]
    index_array = [1, 0, 2]
    expected_output = [11,10, 12]
    format_and_print(array, index_array, expected_output)