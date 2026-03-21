###1. Define a node classwith instance member variable item, prority    and next
class Node:
    def __init__(self,next= None, prev = None, item = None, priority = None):
        self.item = item
        self.next = next
        self.prev = prev
        self.priority = priority

###2. define a class PriorityQueue to implement priority queue data structure using singly linked list . Provide __init__() method to create a start reference varialble
##(intially containaing NOne) and item_count variable (intially 0)
class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
        
###3. Define is_empty method in PriorityQueeue class to check if the preior queeue is emtpy or not
    def is_empty(self):
        return self.start is None
    
###4. Define a push method in PriorityQueue class to insert new data with given priority 
    def push(self, item, priority):
        new_node = Node(item,priority)
        if self.is_empty():
            self.start = new_node
            self.item_count += 1
            return
        
        temp = self.start
        while temp is not None:
            if new_node.priority > temp.priority:
                if temp is self.start:
                    self.start.prev = new_node
                    new_node.next = self.start
                    self.start = new_node
                    self.item_count +=1
                    return
                elif temp is not self.start:
                    before_node = temp.prev
                    new_node.prev = temp.prev
                    temp.prev = new_node
                    new_node.next = temp
                    before_node.next = new_node
                    self.item_count += 1
                    return
            if temp.next is None:
                temp.next = new_node
                new_node.prev = temp
                self.item_count += 1
                return
            temp = temp.next    

###5. define pop method in priority queeu class, whch returns the highest priority data stored in the priority queue data struture .
##raise exception if priority queue is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError("list is empty")
        start_item = self.start.item
        if self.start.next is None:
            self.start = None
            self.item_count -= 1
            return start_item
        self.start = self.start.next
        self.start.prev = None
        self.item_count -= 1
        return start_item

##6 In a class priorityqueue, define a method size to return the number of elements present in the priority queue.
    def size(self):
        return self.item_count 
        