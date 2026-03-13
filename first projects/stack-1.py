###1. define a class STack to implement stack data structure using __init__() method to create an empty list object as instance object memeber stack
class stack:
    def __init__(self):
        self.items = []

###2. Define a method is_empty() to check if the stack is empty in stack class
    def is_empty(self):
        # if self.items == []:
        #     return True
        
        return len(self.items) == 0
            
        
###3 In a stack class, define push() to add data on the stack
    def push(self, data):
        self.items.append(data)
        
###4. In a stack class, define pop() method to remove the top   elememnt form the stack
    def pop(self):
    #     if len(self.items) == 0:
    #         return None
    #     return self.items.pop()
    
        if not self.is_empty():
             return self.items.pop()
        else:
            raise IndexError("stack is empty")
    

###5. In a stack class, define peek() method to return the top elemnt form the stack 
    def peek(self):
        # if len(self.items) == 0:
        #     return None
        # return self.items[-1]
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("stack is empty")
    

###6. in a stack class define size() method to return the size of the stack that is number of items present in the stack
    def size(self):
        return len(self.items)
    
e = stack()
e.push(10)
e.push(20)
e.push(30)
print(f"top element is {e.peek()}")