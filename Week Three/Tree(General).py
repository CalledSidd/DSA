class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def printTree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.printTree()

def build_tree():
    root = TreeNode("Devices")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Maacbook"))
    tablet = TreeNode("Tablet")
    tablet.add_child(TreeNode("iPad"))
    phone = TreeNode("Phone")
    phone.add_child(TreeNode("iPhone"))
    root.add_child(laptop)
    root.add_child(tablet)
    root.add_child(phone)
    return root

if __name__ == '__main__':
    root = build_tree()
    root.printTree()
    pass