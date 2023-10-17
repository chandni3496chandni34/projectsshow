class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None  # Return None for an empty stack, you can raise an exception if you prefer

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None  # Return None for an empty stack, you can raise an exception if you prefer

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
# Create a stack
my_stack = Stack()

# Push elements onto the stack
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# Peek the top element
print(my_stack.peek())  # Output: 15

# Pop elements from the stack
print(my_stack.pop())   # Output: 15
print(my_stack.pop())   # Output: 10

# Check if the stack is empty
print(my_stack.is_empty())  # Output: False

# Get the size of the stack
print(my_stack.size())      # Output: 1
