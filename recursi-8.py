##write a python function to print the revere of given number

def rev(n, r_sum = 0):

    if n == 0:
        return r_sum
    
    r = n % 10
    r_sum = r_sum * 10 + r
    return rev(n // 10, r_sum)
    

a = int(input("Enter the number for the reverse::"))
print(f"The reverse of the number {a} is {rev(a)} ")