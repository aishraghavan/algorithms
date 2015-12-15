
class _double_linked_list_Node:
    def __init__(self, contents=None, prev=None, next=None):
        self.contents = contents
        self.prev = prev
        self.next = next

    def getContents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)
        #return "prev: {0} -> Node: {1} -> next: {2}".format(self.prev, str(self.contents), self.next)
