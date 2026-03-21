##1. define a class Node with instance object member variable prev, item and next.
class Node:
    def __init__(self,item = None, prev= None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
#2. define a class Deque to implement deque data structure using doubly linked list coucept. Define __init__() method to intialise front and rear reference variable
##item_count variable to keep track of number of elements in the deque.
class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.item_count = 0
##3 define a method is_empty() to heck if the deque is empty in Deque class.
    def is_empty(self):
        if self.front is None:
            return True
        return False
    
##4. In deque class, define insert_front() method to add data at the front of the deque
    def insert_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.item_count += 1
            return
        self.front.prev = new_node
        new_node.next = self.front
        self.front = new_node
        self.item_count += 1
##5. in Deque class, define insert_rear() method to add data at the rear of the deque.
    def insert_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.rear = new_node
            self.front = new_node
            self.item_count += 1
            return
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node
        self.item_count += 1
##6. IN deque class, define delete_front() method to remove front element form the deque
    def delete_front(self):
        if self.is_empty():
            raise IndexError("list is empty")
        if self.front == self.rear:
            self.front = None
            self.rear = None
            self.item_count -= 1
            return
        self.front = self.front.next
        self.front.prev = None
        self.item_count -= 1
        
##7. In deque class, define delete_rear()method to remove rear element for the deque.
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("list is empty")
        if self.rear == self.front:
            self.rear = None
            self.front = None
            self.item_count -= 1
            return
        temp = self.rear.prev
        temp.next = None
        self.rear = temp
        self.item_count -= 1
##8. In deques class, define get_front() method to return fornt element form the deque
    def get_front(self):
        if self.is_empty():
            raise IndexError("list is empty")
        return self.front.item
##9. In Deque class, define get_rear() method to return rear element of the deque.
    def get_rear(self):
        if self.is_empty():
          raise IndexError("list is empty")
        return self.rear.item
##10. In Deque class, define size() method to return size of the deque that is number of items present in the deque
    def size(self):
        return self.item_count
      
    
                
        
         
            
            
            