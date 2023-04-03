class Node:
    def __init__(self, data):
        self.data = data
        self.ref  = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            raise Exception("Linked list is empty")
        else:
            n = self.head 
            while n :
                print(n.data, "--->", end=" ")
                n = n.ref

    def add_front(self, data):
        node = Node(data)
        node.ref = self.head
        self.head = node

    def add_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            n = self.head 
            while n.ref:
                n = n.ref
            n.ref = node

    def del_front(self):
        if self.head is None:
            raise Exception("Linked list is empty")
        else:
            self.head = self.head.ref


    def insert(self, index, data):
        count = 0
        n = self.head 
        while n:
            if count == index - 1:
                node = Node(data)
                n.ref = node
                break
            n = n.ref
            count += 1

    def delete(self, index):
        if index == 0:
            self.head = self.head.ref 
            return
        count = 0
        n = self.head 
        while n:
            if count == index - 1:
                n.ref = n.ref.ref
                break
            n = n.ref
            count += 1



ll = LinkedList()
ll.add_front(19)
ll.insert(1, 20)
ll.add_end(21)
ll.insert(3, 22)
ll.add_end(23)
ll.delete(4)
ll.print()