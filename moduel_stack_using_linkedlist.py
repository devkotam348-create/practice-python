##1. import module containig singly linked list code in your python file
import stack_using_linkedlist

##2. Define a class Stack to implement stack data structure. Define __init__() method to create singly Linked List(SLL) object.
class Stack:
    def __init__(self):
        self.SLL = stack_using_linkedlist.Stack()
        
##3. Define a method is_empty() to check if the stack is emty is Stack class.
    def is_empty(self):
       return self.SLL.is_empty()
        
##4. In stack class, define push() method to add data onto the stack class
    def push(self,item):
       self.SLL.push(item)
       
##5. In a stack class, define pop() method to remove top element from the stack
    def pop(self):
        return self.SLL.pop()
##6. In stack class, define peek() method to return top element on the stack
    def peek(self):
     return self.SLL.peek()
##7. In stack class, define size() method to return size of the stack that is number of items present in the stack
    def size(self):
        return self.SLL.size()

e = Stack()
e.push(10)
print(e.peek())
print(e.size() )
e.pop()
print(e.size())
e.pop()
print(e.size())