##queue using singly list class
class Node:
    def __init__(self, item = None, next_node = None):
        self.item = item
        self.next = next_node
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    def is_empty(self):
      if self.front is None:
          return True
      return False
    def enqueue(self, item):
            new_node = Node(item)
            if self.front is None:
                self.front = new_node
                self.rear = new_node
                self.count += 1
                return
            self.rear.next = new_node
            self.rear = new_node
            self.count += 1
    def dequeue(self):
        if self.front is None:
            raise IndexError("queue is empty")
        item = self.front.item
        if self.front == self.rear:
            self.front = None
            self.rear = None
            self.count -= 1
            return item
        self.front = self.front.next
        self.count -= 1
        return item
    def get_front(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.rear.item
    def size(self):
        return self.count

    