##write rescursive fucntion to calculate factorial of a given number

def fact(n):
    
    if n == 0:
        return 1
    
    return n * fact(n-1)

n = int(input("Enter the number for factorial::"))
print(f"The factorial of {n} is {fact(n)}")
