"""
str to list
"""
a='hello world'
map(lambda x:x, a)


"""
reverse in place
"""
[::-1]


"""
if and for in one line
if first then for
"""
temp_list = [lista[i] if i<len(lista) else 0 for i in range(length)]


"""
Range reverse
"""
>>> range(9,-1,-1)
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> range(-2, 6, 2)
    [-2, 0, 2, 4]


"""
ASCII
"""
>>> ord('a')
97
>>> chr(97)
'a'
>>> chr(ord('a') + 3)
'd'
