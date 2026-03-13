## 1. define a class Node to describe a node of a circular doubly linked list.
class Node:
    def __init__(self, item = None, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
        
##2. Define a class CDLL to implement Circular Doubly LInked list with __init__ () method to create and intialise last refrecne variable
class CDLL:
    def __init__(self):
         self.tail = None
##3.Define method empty() to check if th elinked list is empty in CDLL class.

    def empty(self):
        if self.tail is None:
            return True
        return False

##4. In a class CDLL define a method insert_at_start() to insert an element at the starting of the list 
    def insert_at_start(self, item):
        new_node = Node(item)
        if self.tail is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.tail = new_node
            return
        
        start = self.tail.next
        temp = start
        self.tail.next = new_node
        new_node.next = temp
        new_node.prev = self.tail
        start.prev = new_node

##5. Ina class CDLL, define a method isert_at_last() to insert an element at the end of the list
    def insert_at_last(self,item):
        new_node = Node(item)
        if self.tail is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.tail = new_node
            return
        start = self.tail.next
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = start
        start.prev = new_node
        self.tail = new_node
        
##6. in a class CDLL define a method search() to find the node with specified element
    def search(self, item):
        if self.tail is None:
            return None
        start = self.tail.next
        temp = start
        while True:
            if temp.item == item:
                return True
            temp = temp.next
            if temp == start:
                break
        return None
##7. In a class CDLL, define a method isert_after() to insert a new node after a given node of the list .
    def insert_after(self,old_item, new_item):
        new_node = Node(new_item)
        if self.tail is None:
            return False
        if self.tail.item == old_item:
            self.insert_at_last(new_item)
            return True
        
        start = self.tail.next
        temp = start
        while True:
            if temp.item == old_item:
                after = temp.next
                new_node.next = after
                temp.next = new_node
                new_node.prev = temp
                after.prev = new_node
                return True
            temp = temp.next
            if temp == start:
                break
        return False
            
### 8. in a class CDLL, define a method to print all the elements of the list
    def is_show(self):
        store = []
        if self.tail is None:
            return []
        start = self.tail.next
        temp = start
        while True:
            store.append(temp.item)
            temp = temp.next
            if temp == start:
                break
        return store

##9. In a CDLL, implement iterator for CDLL to access all the elements of the list in a sequence.
    def __iter__(self):
        if self.tail is None:
            return
        start = self.tail.next
        temp = start
        while True:
            yield temp.item
            temp = temp.next
            if temp == start:
                break
            
##10. In a CDLL, define a method delete_first() to delete the first item from the list
    def delete_first(self):
        if self.tail is None:
            return None
        if self.tail.next == self.tail:
            self.tail = None
            return
            
        start = self.tail.next
        after = start.next
        after.prev = self.tail
        self.tail.next = start.next
        
##11. In a CDLL, define a method delete_last() to delete the last item form the list
    def delete_last(self):
        if self.tail is None:
            return None
        if self.tail.next == self.tail:
            self.tail = None
            return
        start = self.tail.next
        second_last = self.tail.prev
        second_last.next = start
        start.prev = second_last
        self.tail = second_last
        
##12. in  CDLL, define a method delete_item() to delete specified item from the list
    def delete_item(self, item):
        if self.tail is None:
            return None
        start = self.tail.next
        if start.item == item:
            self.delete_first()
            return True
        if self.tail.item == item:
            self.delete_last()
            return True
        temp = start
        while True:
            if temp.item == item:
                before = temp.prev
                after = temp.next
                before.next = after
                after.prev = before
                return True
            temp = temp.next
            if temp == start:
                break
        return False
        
        

        


e = CDLL()
e.insert_at_start(22)
e.insert_at_start(44)
print(e.is_show())
e.insert_at_last(33)
print(e.is_show())
print(e.search(33))
e.insert_after(44,99)
print(e.is_show())
e.insert_after(22,100)
print(e.is_show())
e.insert_after(55,100)
e.delete_first()
print(e.is_show())
e.delete_last()
print(e.is_show())
e.delete_item(22)
print(e.is_show())