# you can use the collection modle and the deque class 
import collections

stack = collections.deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)
stack.pop()
print(stack)

# using the queue module LifoQueue 
import queue
stack = queue.LifoQueue(4)
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
stack.put(5, timeout=1)
print(stack)
stack.get()
print(stack)