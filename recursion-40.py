##write a recursive fucntion to calculate sum of digits of a given number.

def calculate(n):
    
    if n == 0:
        return 0
    
    return (n%10) + calculate(n//10)

n = int(input("Enter the dight::"))
r = calculate(n)
print(f"The sum of the digit is {r}")
