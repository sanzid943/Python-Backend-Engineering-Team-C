
def create_stack():
    return [] # list as a stack

def push(stack, item):
    stack.append(item)

def pop(stack):
    try:
        return "Popped item: " + str(stack.pop())
    except IndexError:
        raise IndexError("pop from an empty stack")

def top(stack):
    try:
        return "Top item: " + str(stack[-1])
    except IndexError:
        raise IndexError("top from an empty stack")

def is_empty(stack):
    if len(stack) == 0:
        return "stack is empty"
    else:
        return  "stack is not empty"

def size(stack):
    return "size of the stack: " + str( len(stack) )


# Example usage
stack = create_stack()

push(stack, 1)
push(stack, 2)
push(stack, 3)
print(stack)          # [1, 2, 3]

print(pop(stack))     # 3
print(top(stack))    # 2
print(size(stack))    # 2
print(is_empty(stack)) # False

# Emptying the stack and testing error handling
try:
    print(pop(stack))  # works fine, stack is not empty
except IndexError as e:
    print("Error:", e)
try:
    print(pop(stack))  # works fine, stack is not empty
except IndexError as e:
    print("Error:", e)

try:
    print(pop(stack))  # stack is now empty
except IndexError as e:
    print("Error:", e) # catches & shows error

try:
    print(top(stack))  # stack is empty
except IndexError as e:
    print("Error:", e) # catches & shows error