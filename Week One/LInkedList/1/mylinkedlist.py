class Node:
    def __init__(self, data):
        self.data = data,
        self.link = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def print(self):
        if not self.head:
            raise Exception('List is empty')
        else:
            n = self.head 
            while n :
                print(n.data, '>>>' , end=" ")
                n = n.link

    def add_head(self, data):
        node = Node(data)
        node.link = self.head 
        self.head = node

    def add_tail(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            n = self.head
            while n.link:
                n = n.link
            n.link = node

    def delete_node(self, index):
        try:
            if index == 0:
                self.head = self.head.link
                return 
            count = 0
            n = self.head
            while n:
                if count == index -1:
                    n.link = n.link.link
                    break
                n = n.link
                count += 1
        except:
            print("Invalid")




linkedlist = LinkedList() 

linkedlist.add_head(13)
linkedlist.add_head(12)
linkedlist.add_tail(14)
linkedlist.delete_node(0)
linkedlist.print()