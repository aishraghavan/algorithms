"""
https://www.careercup.com/question?id=5631950045839360

write a method that takes in 2 int arrays of any size and returns an array that calculates the sum of both.

for example, [1,2,3] and [2,3,4] will return [3,5,7]

Or [1,2,3] and [2,3,5,5] will return [2,4,7,8]

however, if it's like [9,9,2] and [0,1,3] you need to carry the sum so it returns as [1,0,0,5]

** SINGLE DIGIT ONLY
"""

def sum_of_arrays(lista, listb):
    max_len=max(len(lista), len(listb))
    lista = fill_with_zeros(lista, max_len)
    listb = fill_with_zeros(listb, max_len)
    print "lista : {0}", lista
    print "listb : {0}", listb
    input_arrays = zip(lista, listb)
    output_list = []
    temp = 0

    for index in range(max_len-1, -1, -1):
        a = lista[index]
        b = listb[index]
        sum = a + b + temp
        temp = 0
        if sum<10:
            output_list.append(sum)
        else:
            temp = sum/10
            output_list.append(sum%10)
    if temp != 0:
        output_list.append(temp)
    output_list = output_list[::-1]
    print "output_list :{0}".format(output_list)


def fill_with_zeros(lista, length):
    if len(lista) == length:
        return lista
    diff_len = length - len(lista)
    temp_list = [0 if i<diff_len else lista[i-diff_len] for i in range(length)]
    return temp_list


# a = [1,2,3,4,5,6]
# b = [2,3,4,5,6,7,8]
# sum_of_arrays(a,b)

a = [9,9,2]
b = [1,3]
sum_of_arrays(a,b)

a = [1,2,3]
b = [2,3,5,5]
sum_of_arrays(a,b)
