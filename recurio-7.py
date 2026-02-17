##write a python function to print square of fir n numbers

def even(n):

    if n == 0:
        return 
    
    
    even(n-1)
    print(n**2, end = " ")
    

r = int(input("Enter the nth number::"))
even(r)