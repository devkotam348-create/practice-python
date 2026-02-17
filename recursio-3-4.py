##write a pyhton funciton that calculates the sum square of first n natural nubmers

def adding(n):

    if n == 0:
        return 0
    
    return (n**2) + adding(n-1)

r = int(input("Enter the nth value::"))
print(f"The sum of square of first natural number is {adding(r)}")
