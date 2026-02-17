##write a recursive function to print first N odd natural numbers

def odd(n):

    if n == 0:
       return
    
    odd(n - 1)
    print(2*n -1)
     
r = int(input("Enter the nth number::"))
odd(r)
     

     