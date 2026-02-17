##write a python funciton to calculate HCF (highest Common Factor) of a list of numbers. Use reduce function 

from functools import reduce
def HCF(a,b):
    
    limit = min(a,b)
    h = 1

    for l in range(2, limit+1):
        if a % l == 0 and b % l == 0:
            h = l
    return h
    

  



s = [12, 10, 4, 14, 18]
result = reduce (lambda a,b: HCF(a,b),s)
print (result)