###Define a class Deque to implement deque data structure using list. Define __init__()method to create an empty list object as instance object memeber of Deque
class Deque:
    def __init__(self):
        self.data = []
    

###2. define a method is_empty() to check if the deque is empty 
    def is_empty(self):
        return len(self.data) == 0

###3.In Deque class, define insert_front() method to add data at the front end of the deque
    def insert_front(self, item):
       self.data.insert(0,item) 
     

###4. In deque class define insert_rear() mehtod to add daa at the rear end of the deque.
    def insert_rear(self, item):
        self.data.append(item)
      
           
###5. In Deque class, define delete_front() method to remove front element form the deque.
    def delete_front(self):
        if self.is_empty():
            raise IndexError("list is empty")
        self.data.pop(0)
        
###6 . In Deque class, define delete_rear() method to remove rear element form the deque.
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("list is empty")
        self.data.pop()
        

###7. In Deque class, define get_front() method to return front element of the deque.
    def get_front(self):
        if self.is_empty():
            raise IndexError("list is empty")
        return self.data[0]

###8. in Deque clas, define get_rear() method return rear element of the deque.
    def get_rear(self):
        if self.is_empty():
            raise IndexError("list is empty")
        return self.data[-1]
    
###9. in deque class, define size() method to return size of the deque that is number of items present in the deque.
    def size(self):
        return len(self.data)
    

e = Deque()

e.insert_front(10)
e.insert_rear(20)
print(e.get_front())
print(e.size())

        