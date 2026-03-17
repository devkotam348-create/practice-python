##1. import module containing linked list code in your python file 
import stack_using_linkedlist

##2. Define a class Stack to implement stack data struture by inherting SLL class
class Stack(stack_using_linkedlist.Stack):
    pass

##3. define a method is_empty() to check if the stack is empty in Stack class
    def is_empty(self):
        return super().is_empty()
        
##4. In stack class define a push() method to add data on a stack 
    def push(self, item):
        super().push(item) 
        
##5. in a stack class define a pop() method to remove top element form the stack
    def pop(self):
        return super().pop()
    
##6. In a stack class define peek()nmethod to return top element of the stack
    def peek(self):
        return super().peek()

##7. In stack class define size() method to return the size of the stack that is number of item presents in stack
    def size(self):
        return super().size()
    
    
e = Stack()
e.push(10)
print(e.peek())
print(e.size())