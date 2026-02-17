##write a recursive function to print first N odd natural number in reverse order 

def odd(n):
     
     if n == 0:
        return
     print(2*n - 1)
     odd(n-1)

r = int (input("Enter the nth number::"))
odd(r)