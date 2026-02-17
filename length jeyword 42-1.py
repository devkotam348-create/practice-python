###write a fucntion which receives variable length arguments to calculate average of integers. It returns the average of numbers.

def avg(*t):
   
   size = len(t)
   average = sum(t)/size

   return average

r = (1,2,3,4)
result = avg(*r)
print(f"The average is {result}")

