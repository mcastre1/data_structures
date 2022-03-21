class Stack():
    '''Implementation of a stack and basic functions in python.'''
    
    def __init__(self):
        # Constructor to the Stack class, creates an empty list.
        self.items = []

    def push(self, item):
        # Appends the given item to the list, items.
        self.items.append(item)

    def pop(self):
        # Returns and removes the last item in the items list.
        return self.items.pop()

    def peek(self):
        # Returns the last item in the items list, without removing it.
        return self.items[-1]

    def isEmpty(self):
        # Checks whether the items list is empty or not.
        return self.items == []

    def size(self):
        # Retunrs the lenght of items list. 
        return len(self.items)



# Making sure the stack works as intended.
stack = Stack()

print(stack.isEmpty())
stack.push(1)
stack.push("two")
print(stack.peek())
stack.push(True)
print(stack.size())
print(stack.isEmpty())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())