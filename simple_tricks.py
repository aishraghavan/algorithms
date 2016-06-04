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
