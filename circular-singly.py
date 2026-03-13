###1. define a class node to describe a node of a circularlinked list

class Node:
    def __init__(self, item = None, next_node = None):
        self.item = item
        self.next = next_node
        
###2. define a class CLL to implement Circular Linked List with __init__() method to create and intialise last reference variable 
class CLL:
    def __init__(self):
        self.tail = None

###3. define a method is_empty() to check if the linked list is empty CLL class
    def is_empty(self):
        if self.tail is None:
            return True
        return False
    
###4. in a class CLL, define a method insert_at_start() to insert an element at starting of the list
    def insert_at_start(self, item):
        New_Node = Node(item)
        if self.tail is None:
            self.tail = New_Node
            New_Node.next = New_Node
            return
        old_first = self.tail.next
        New_Node.next = old_first
        self.tail.next = New_Node
###5. In class CLL, define a method inser_at_last() to insert an element at the end of the list.
    def insert_at_last(self,item):
        New_Node= Node(item)
        if self.tail is None:
            self.tail = New_Node
            New_Node.next = New_Node
            return
        old_first = self.tail.next
        self.tail = New_Node
        New_Node.next = old_first
        self.tail = New_Node
###6. In a class CLL, define a method search() to find the node with specified elemetn value.
    def search(self,item):
        if self.tail is None:
          return False
    
        start = self.tail.next
        temp = start
        while True:
            if temp.item == item:
                return True
            temp = temp.next
            
            if temp == start:
                break 
        return False
        
###7. In a class CLL, define a method insert_after() to insert a new node after a given node of the list
    def insert_after(self,old_value, new_value):
        New_Node = Node(new_value)
        if self.tail is None:
            return False
        
        start = self.tail.next
        temp = start
        while True:
            if temp.item == old_value:
                New_Node.next = temp.next
                temp.next = New_Node
                if temp == self.tail:
                    self.tail = New_Node
                return True
            temp = temp.next
            if temp == start:
                break
        return False

###8.In a CLL, define a to print all the elemets of the list
    def is_show(self):
        show = []
        if self.tail is None:
            return False
        start = self.tail.next
        temp = start
        
        while True:
            show.append(temp.item)
            temp = temp.next
            if temp == start:
                break
            
            
                
        return show

###9.In a class CLL, implemet iterator for CLL to acess all the elemetns of the list in a sequence
    def iterator(self):
        it =iter(self.is_show())
        return it
        
###10. In a class CLL, define a method delete_first() to delete first elemets of the list in a sequence
    def delete_first(self):
        if self.tail is None:
            return False
        first_node = self.tail.next
        if self.tail.next == self.tail:
            self.tail = None
            return
        self.tail.next = first_node.next
        
##11. In a class CLL, define a method delete_last() to delete last element form the list
    def delete_last(self):
        if self.tail is None:
            return False
        start = self.tail.next
        temp = start
        if start == self.tail:
           self.tail = None
           return 
        while True:
            if temp.next == self.tail:
                temp.next = start
                self.tail = temp
                return True
            temp = temp.next
            if temp == self.tail:
             break
         
##12. In a class CLL, define a method delete_itm() to delete specified element form the list. 
    def delete_item(self,item):
        if self.tail is None:
            return False
        start = self.tail.next
        temp = start
        if temp.item == item:
            self.delete_first()
            return
        if self.tail.item == item:
            self.delete_last()
            return
       
        while True:
            current = temp.next
            if current.item == item:
                temp.next = current.next
                return True
            temp = temp.next
         
            if temp == self.tail:
                break
        return False
         
         
    
    
    
    
e = CLL()

e.insert_at_start(10)
print(e.is_show())
e.insert_after(10,20)
print(e.is_show())
it = e.iterator()
print(next(it))

            
            
            
        
        