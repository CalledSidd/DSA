# queue = list()

# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)

# queue.pop(0)
# print(queue)
queue = list()
def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element, " Added")

def dequeue():
    if not queue:
        print("Queue empty")
    else:
        element = queue.pop(0)
        print(element, " Removed") 

def display():
    print(queue)

while True:
    print('Choose \n 1.Add \n 2.Remove \n 3.Show \n 4.Quit ')
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Improper")
