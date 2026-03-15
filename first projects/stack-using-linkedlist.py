##1. define a class stack to implement stack data structure using singly linked list concept. Define __int__() method to initialsize start reference variable and item_count
### variable to track of number of items in the stack
class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
            self.start = None
            self.item_count = 0
            
##2. define a method is_empty() to check if the stack is empty in empty class
    def is_empty(self):
            return self.start is None
        
##3. In a stack class, define push() method to add onto the stack:
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.start
        self.start = new_node
        self.item_count += 1
        
##4. in stack class, define pop() method to remove top element form the stack
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is emtpy')
        temp = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return temp
        
##5. In stack class, define peek() method to return top element of the stack.
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is emtpy')
            
        return self.start.item
        
##6. In a stack class,define size() method to return size of the stack that is number of items present in the stack
    def size(self):
        return self.item_count
    
    
    
e = Stack()
e.push(10)
e.push(20)
e.push(30)

print(e.size())
print(e.peek())
e.pop() 
print(e.size())
print(e.peek()) 
    

        