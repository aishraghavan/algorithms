from _tree import Tree

def least_common_ancestor_in_bst_recursive(root, n1, n2):
    if root == None: #or n1 == None or n2 == None:
        return
    if n1 < root.data and n2 < root.data:
        return least_common_ancestor_in_bst_recursive(root.left, n1, n2)
    if n1 > root.data and n2 > root.data:
        return least_common_ancestor_in_bst_recursive(root.right, n1, n2)
    return root


if __name__ == "__main__":
    l1 = Tree(5)
    l2 = Tree(7)
    l3 = Tree(9)
    l4 = Tree(20)
    m1 = Tree(6, l1, l2)
    m2 = Tree(10, l3, l4)
    root = Tree(8, m1, m2)
    print least_common_ancestor_in_bst_recursive(root, 5, 6)
    print least_common_ancestor_in_bst_recursive(root, 5, 20)
    print least_common_ancestor_in_bst_recursive(root, 9, 20)
