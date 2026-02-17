##write a function to calculate sum of first n Natural number

def natural(n):

    if n == 0:
      return 0
    
    sum = n + natural(n-1)
    return sum
r = int(input("Enter the nth number::"))
print(f"The sum of {r}th is {natural(r)}")