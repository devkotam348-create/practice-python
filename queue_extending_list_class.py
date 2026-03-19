###1. Define a class queue to implement queue Data structure by extending list class 
class Queue(list):

###2. Define a method is_empty to check if the stack is empty in queue  class
    def is_empty(self):
        return len(self) == 0
###3.  defina a method enque() to insert the data in the  queue
    def enqueue(self, data):
        self.append(data)

    
###4. define a method dequeue() method to delete the data in the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
    
        return super().pop(0)
## define a method get_first() method to display the item of the first
    def get_first(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        return self[0]
## 6. deofne a method get_last() to get the last of the list
    def get_last(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        return self[-1]
### 7. get the size of the list
    def size(self):
        return len(self)
            
        
   
   