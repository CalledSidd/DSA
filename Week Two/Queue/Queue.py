queue = []

def enqueue(value):
    queue.append(value)

def dequeue():
    if queue:
        queue.pop(0)
    else:
        print("Queue is empty")

def display():
    print(queue)


enqueue(5)
enqueue(6)
dequeue()
display()