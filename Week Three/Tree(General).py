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

laptop = TreeNode("Laptop")
laptop.add_child("MacBook")
laptop.add_child("HP Pavillion")
laptop.add_child("Razer Blade")

phone = TreeNode("Smart Phone")
phone.add_child("iPhone")
phone.add_child("Pixel")
phone.add_child("ROG Phone")

watch = TreeNode("Smart Watch")
watch.add_child("Apple watch")
watch.add_child("realme watch")
watch.add_child("pixel watch")

root = TreeNode("Devices")
root.add_child(laptop)
root.add_child(phone)
root.add_child(watch)