"""
https://www.careercup.com/question?id=5692987154628608

There are 2 arrays of integers.You have to add the those integers and keep it in 3rd array.there is one condition, if the sum is a 2 digit number, split that number into single digiit and other condition is if any of the array integer is left then print that number
I/P:
int[] a = {1,2,3,4,5,6}
int[] b = {2,3,4,5,6,7,8}
o/p:
{3,5,7,9,1,1,1,3,8}
"""

def sum_of_arrays(lista, listb):
    max_len=max(len(lista), len(listb))
    lista = fill_with_zeros(lista, max_len)
    listb = fill_with_zeros(listb, max_len)
    input_arrays = zip(lista, listb)
    output_list = []
    for a,b in input_arrays:
        sum = a +b
        if sum<10:
            output_list.append(sum)
        else:
            output_list.append(sum/10)
            output_list.append(sum%10)
    print "lista :{0}".format(lista)
    print "listb :{0}".format(listb)
    print "output_list :{0}".format(output_list)


def fill_with_zeros(lista, length):
    temp_list = [lista[i] if i<len(lista) else 0 for i in range(length)]
    return temp_list


a = [1,2,3,4,5,6]
b = [2,3,4,5,6,7,8]

sum_of_arrays(a,b)
