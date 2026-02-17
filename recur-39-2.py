#write a python recursive function to calculate the sum of n odd natural number 

def addo(n, nsum = 0):
    
    if n == 0:
       return nsum
    nsum = nsum + (2* n -1)
    return addo(n-1, nsum)
    
a = int(input("Enter the nth number::"))
r = addo(a)
print(f"The sum of odd number is {r}")


#write a python recursive function to calculate the sum of n even natural number     

def addo(n):
    
    if n == 0:
        return 0
    return (2*n) + addo(n -1 )

r = int(input("Ennter the nth number::"))
print(f"The sum of nth even number is {addo(r)}")
    
    