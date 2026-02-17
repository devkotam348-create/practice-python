##write a recursive function to print firs N natural numbers in reverse order 
def reverse(n):
    if n == 0:
       return
    
    print(n)
    reverse(n-1)


r = int(input("Enter the number::"))
reverse (r)