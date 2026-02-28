##1. define a class Node to describe a node of singly linked list.

class Node:
    def __init__(self, item = None, next_node = None):
        self.item = item
        self.next = next_node

##2 .Define a class SLL to implemet Singly Linked LIst with __init__() mmethode to create and initialist start reference valriable 

class SLL:
    def __init__(self):
        self.start = None

## 3. Define a method is_empty() to check if the linked list is empty in SLL class
    def is_empty(self):
        return self.start is None
    
## 4. in class SLL, define a method inser_at_start() to insert and element at the starting of the list 
    def insert_at_start(self, item):
        new_node = Node(item)
        new_node.next = self.start
        self.start = new_node

## 5. in class sLL, define a method inset_at_last() to insert an elemnt at the end of the list 

    def insert_at_last(self, item):
        prev = self.start
        if self.start is None:
            self.insert_at_start(item)
            return
        new_node = Node(item)
        while prev.next is  not None:
            prev = prev.next
        prev.next= new_node
        
## 6. In class SLL, define a method search()to find the with specified element 

    def search(self, item):
        prev = self.start
        while prev is not None:
           if prev.item == item:
               return True
           prev = prev.next

        raise ValueError(f"{item} is not found on the list")
            
###7. in class SLL, define a method insert_after() to insert a new node after a given node of the list 
    def insert_after(self,old_node, new_node):
        new_node = Node(new_node)
        prev = self.start
       
        while prev is not None:
            if prev.item == old_node:
                new_node.next = prev.next
                prev.next = new_node
                return
            prev = prev.next
        raise ValueError(f"{old_node} is not found in the list")
    
###8. In a class SLL, define a method to print all the element of the list

    def Show_data(self):
        value = []
        prev = self.start

        while prev is not None:
            value.append(prev.item)
            prev = prev.next
        return value
    
##9. In class SLL, implemet iterator for SLL to access all the elemets of list in a sequence.
    
    def __iter__(self):
        prev = self.start
        while prev is not None:
            yield prev.item
            prev=  prev.next

##10. In class SLL, define a method delete_first()to delete first element from the list
    
    def delete_first(self):
        if self.start is None:
            raise ValueError('List is empty')
        self.start= self.start.next
##11. In class SLL, define a method delete_item()to delete specified element firm the list

    def delete_item(self, item):
        prev = None
        current = self.start
        while current is not None:
            if current.item == item:
                if prev is None:
                    self.start = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next
        raise ValueError("not found")
    ##12 In class SLL, define a method delete_last() to delete last element form the list
    def delete_last(self):
        prev = None
        current = self.start 
        if current is None:
            raise ValueError("list is empty")
        elif current.next == None:
            self.start = None
            return
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
                
            
        
     
        

            
            

e = SLL()
e.insert_at_start(10)
e.insert_at_last(20)
e.insert_at_last(30)
print(e.Show_data())
e.insert_after(20, 50)
print(e.Show_data())
for x in e:
    print(x)
e.delete_first ()
print(e.Show_data()) 

