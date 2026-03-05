##1. Define a class Node to describe a node of a doubloy linked list

class Node:
    def __init__(self, item = None, prev_ref = None,  next_ref = None):
        self.item = item
        self.prev = prev_ref
        self.next = next_ref 
##2. define a class DLL to implement Doubly Linked list with __init__() method to create and initialise start reference variable

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None 

##3. define a methos is_empty() to check if the linked list is empty in DLL class
    def is_empty(self):
        return self.head is None
    
    

##4. In a class DLL, define a method insert_at_start() to insert an element at the starting of the list

    def insert_at_start(self, item):
        New_node = Node(item)
        prev = self.head
        if prev is None:
            self.head = New_node
            self.tail = New_node
        else:
            New_node.next = self.head
            self.head.prev = New_node
            self.head = New_node
        
##5. In class DLL, define a method insert_at_last_() to insert an element at the end of the list
    def insert_at_last(self, item):
        New_node = Node(item)
        prev = self.head
        if prev is None:
            self.head = New_node
            self.tail = New_node
            
        else:
           old_tail = self.tail
           old_tail.next = New_node
           New_node.prev = old_tail
           self.tail = New_node
           
## 6. In class DLL, define a method search () to fnf the node with specified element value.
    def search(self, item):
        current = self.head
        while current is not None:
            if current.item == item:
                return current
            current = current.next
        return None

##7 . In a class DLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self,old_node, new_node):
        after = old_node.next
        new_node.next = old_node.next
        old_node.next = new_node
        new_node.prev = old_node
        if after is not None:
            after.prev = new_node
        if old_node == self.tail:
            self.tail = new_node
            
##8 in a class DLL,define a method inser_after_item() to insert a new item after a given iten of the list
    def insert_item_after(self, old_item, new_item):
        temp = self.head
        if temp != None:
            while temp is not None:
                if temp.item == old_item:
                    New_node = Node(new_item)
                    after = temp.next
                    New_node.next = after
                    temp.next = New_node
                    New_node.prev = temp
                    if after is not None:
                        after.prev = New_node
                    if temp == self.tail:
                        self.tail = New_node
                    return
                temp = temp.next
               
        return None
               
##9 In a class DLL, define a method to print all the elements of the list 
   
    def is_show(self):
        show = []
        start = self.head
        while start is not None:
            show.append(start.item)
            start = start.next
        return show
    
#10. In a class DLL, define method delete_first() to delete first element form the list 
    def delete_first(self):
        temp = self.head
        if temp is None:
            return None
        temp = temp.next
        if temp is None:
            self.head = None
            return None
        temp.prev = None
        self.head = temp
        
##11.In a class DLL, define a method delete_last() to delete last element form the list
    def delete_last(self):
        temp = self.tail
        if temp is None:
            return None
        temp = temp.prev
        if temp is None:
            self.tail = None
            self.head = None
            return None
        self.tail = self.tail.prev
        self.tail.next = None
# #12. In a class DLL, define a method delete_item() to delete specified element form the list
#     def delete_item(self,item):
#         current = self.head
#         if current is not None:
#             while current is not None:
#                 if current.item == item:
    

e = DLL()
# num = int(input('insert the number::'))
# e.insert_at_start(num)
# # print(e.is_show())
e.insert_at_start(1)
e.insert_at_start(4)
e.insert_at_last(10)
# num = int(input('Enter the number you want to search::'))
# result = e.search(num)
# if result is None:
#     print('NOt found', result.item)
# else:
#     print('found', result.item)
# old = e.search(4)
# if old is None:
#     print('not found item cant insert')
# else:
#     e.insert_after(old, Node(55))
#     print(e.is_show())
e.insert_item_after(4,22)
print(e.is_show())
e.delete_first()
print(e.is_show())
e.delete_last()
print(e.is_show())


        
        