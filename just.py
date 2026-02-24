
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3

head = n1

count = 0
temp = head 
while temp is not None:
    print(f"{temp.data} ->",end = " ")
    temp = temp.next
    count += 1
print(temp)
print(f'Total nodes::{count}')