###1. Define a class PriorityQueue to implement priority queue daata structure using list. provide __init__() method to create initially empty
class priorityqueue:
    def __init__(self):
        self.data = []
##2 . define is_empty method in priorityqueue class to check if the priority is empty 
    def is_empty(self):
     return len(self.data) == 0
           
###3. Define a push method in priorityqueue class to insert new data given priority
    def push(self, item, priority):
        new_item = (item, priority)
        if self.is_empty():
            self.data.append(new_item)
            return 
        for i in range(len(self.data)):
            if priority > self.data[i][1]:
                self.data.insert(i, new_item)
                return
        self.data.append(new_item)
###4. Define a pop method in priorityqueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority quesue
##is emtpy
    def pop(self):
        if self.is_empty():
            raise IndexError("list is empty")
        return self.data.pop(0)[0]
##5. in a class priorityqueue defina a mthod size to return the number of elements present in the priority queue.
    def size(self):
        return len(self.data)
    
e = priorityqueue()
e.push(2, 5)
e.push(8, 6)
e.push(2,1)

print(e.pop())