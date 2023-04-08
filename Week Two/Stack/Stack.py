stack = list() 

def append(val):
    stack.append(val)

def pop():
    stack.pop()

def display():
    print(stack)

append(5)
append(6)
pop()
display()