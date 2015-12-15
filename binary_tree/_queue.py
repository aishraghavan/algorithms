from _node import Node


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next: last = last.next
            # append the new node
            last.next = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo

    def size(self):
        return self.length

if __name__ == "__main__":
    print "Welcome to Queue"
    queue = Queue()
    for i in range(5):
        num = 10*(i+1)
        print "Inserting {0}".format(num)
        queue.insert(num)

    print "Removing from Queue"
    while not queue.is_empty():
        print  queue.remove()
