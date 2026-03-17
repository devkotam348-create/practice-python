###1. Define a class queue to implement queue data structure using list.Define __init__() method to create an empty list object instance object memeber of queue
class Queue:
    def __init__(self):
        self.item = []
        self.count = 0
###2. define a method is_enpty() to check if the quese is emtpy in queure class
    def is_empty(self):
        return len(self.item) == 0
###3. In a queue class, define enqueue() method to add data at the rear end of the queue
    def enqueue(self, data):
        self.item.append(data)
        self.count += 1
###4. In a queue clas, define dequeue() method to remove front element form the queue
    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is emtpy')
        self.count -= 1
        return self.item.pop(0)
###5. In a queue class, define get_front() method to return front element of the queue
    def get_front(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        return self.item[0]
###6. In a queue class, define get_rear() method to return rear element of the queue.
    def get_rear(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        return self.item[-1]
###7. In a queue class, define size() method to return size of the queue that is number of items present in thhe queue
    def size(self):
        return self.count
    
    
e = Queue()
print(e.size())
e.enqueue(10)
e.enqueue(20)
e.enqueue(30)
e.enqueue(40)
print(e.get_front())
print(e.get_rear())
