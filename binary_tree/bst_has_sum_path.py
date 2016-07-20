from _tree import Tree
from _stacks import Stack

# def has_path_sum(node, sum):
#     if node == None:
#         return False
#         #return (sum == 0)
#     if node.data == sum and (node.left == None and node.right == None):
#         #return (sum - (node.data) == 0)
#         return True
#     else:
#         subsum = sum - node.data
#         return (has_path_sum(node.left, subsum) or
#                 has_path_sum(node.right, subsum))

def has_path_sum_pair(node, sum):
    if node == None:
        return
    stack1 = Stack()
    lista = [] 
    stack1.push(node)
    lista.append(node.data)
    while not stack1.is_empty():
        temp = stack1.pop()
        if not temp.left is None:
            #if temp.left.data < temp.data :
            stack1.push(temp.left)
            lista.append(temp.left.data)
            
        if not temp.right is None:
            stack1.push(temp.right)
            lista.append(temp.right.data)

    for i in range(len(lista)):
        if sum-lista[i] in lista:
            return True
    return False



if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(25)
    l3 = Tree(40)
    l4 = Tree(70)
    m1 = Tree(10, l1, l2)
    m2 = Tree(60, l3, l4)
    root = Tree(30, m1, m2)
    print "has_path_sum of 90 :"
    #print has_path_sum(root, 90)
    print has_path_sum_pair(root, 90)
    print "has_path_sum of 190 :"
    #print has_path_sum(root, 190)
    print has_path_sum_pair(root, 190)
