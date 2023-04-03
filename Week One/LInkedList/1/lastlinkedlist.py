class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return 
        n = self.head 
        while n:
            if n.link is  None:
                n.link = node
                break
            n = n.link
        
    def print(self):
        n = self.head 
        while n:
            print(n.data, '-->', end=" ")
            n = n.link
        print("None")

    def delete(self, index):
        if index == 0:
            self.head = self.head.link
            return 
        count = 0
        n = self.head 
        while n:
            if count == index -1:
                n.link = n.link.link
                return 
            n = n.link
            count += 1

ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.delete(2)
ll.print()