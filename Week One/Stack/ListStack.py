stac = list()

stac.append(12)
stac.append(13)
stac.append(14)
stac.append(15)
stac.append(16)
# print(stac)

stac.pop()
print(stac)
not stac
# print(stac[:-1])

stack = list()

def push():
     element = input("Enter an element : ")
     stack.append(element)
     print(stack)

def pop():
     if not stack:
          print("Stack is empty")
     else:
          e = stack.pop()
          print("Removed the last element",e)
          print(stack)

while True:
     print("Operations \n 1. Push \n 2.Pop \n 3. Quit \n")
     choice = int(input())
     if choice == 1:
          push()
     elif choice == 2:
          pop()
     elif choice == 3:
          break
     else:
          print("Invalid Choice")