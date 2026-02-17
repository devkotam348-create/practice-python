##write a python function to print first n even numbers

def even(n):

    if n == 0:
        return 
    
    
    even(n-1)
    print(2*n, end = " ")
    

r = int(input("Enter the nth number::"))
even(r)