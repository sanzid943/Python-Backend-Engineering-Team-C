from collections import deque

def create_queue():
    return deque()

def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    try:
        return "dequeued item: " + str( queue.popleft() )
    except IndexError:
        raise IndexError("dequeue from an empty queue")

def front(queue):
    try:
        return "front item: " +  str( queue[0] )
    except IndexError:
        raise IndexError("front from an empty queue")

def is_empty(queue):
    if len(queue) == 0:
        return "queue is empty"
    else:
        return "queue is not empty"

def size(queue):
    return "size of the queue: " + str( len(queue) )


# Example usage
queue = create_queue()

enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)
print(queue)           # deque([1, 2, 3])

print(dequeue(queue))  # 1
print(front(queue))     # 2
print(size(queue))     # 2
print(is_empty(queue)) # False

# Emptying the queue and testing error handling
try:
    print( dequeue(queue) ) # works fine, queue is not empty
except IndexError as e:
    print("Error:", e)
try:
    print( dequeue(queue) ) # works fine, queue is not empty
except IndexError as e:
    print("Error:", e)

try:
    print( dequeue(queue) ) # queue is now empty
except IndexError as e:
    print("Error:", e) # catches & shows error

try:
    print( front(queue) )  # queue is empty
except IndexError as e:
    print("Error:", e) # catches & shows error