class Stack: #this code is to mimplemet the stack probelem
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)
my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print(my_stack.pop())  # prints 30
print(my_stack.peek())  # prints 20
print(my_stack.size())  # prints 2