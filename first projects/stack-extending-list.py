###1. Define a class Stack to implement stack Data structure by extending list class 
class Stack(list):
    
###2. Define a method is_empty to check if the stack is empty in stack class
      def is_empty(self):
          return len(self) == 0
      
###3. In a stack class define a push() method to add data on the stack
      def push(self,data):
          self.append(data)
          
###4. In a stack class define a pop() method to remove the top of the element in the stack 
      def pop(self):
          if  self.is_empty():
             raise IndexError("list is empty")
          return super().pop()
      
###5. In a stack class deine a peek() to return top element of the stack 
      def peek(self):
          if self.is_empty():
              raise IndexError("list is empty")
          return self[-1]
      
###6. in a stack define size() method to return size of the stack that is number of items presents in the stack
      def size(self):
          return len(self)
      
###7. Implement the way to restric to use of insert() method of list class form stack object
      def insert(self, index, value):
          raise AttributeError("insert is not allowed in the stack ")

###7. Implement the way to restric to use of remove() method of list class form stack object
      def remove(self, value):
          raise AttributeError("REmove is not allowed in stack")
      
