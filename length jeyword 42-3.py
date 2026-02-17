##write a function which receives a variable length arguments to fileter odd and even numbers. Store all odd numbers in a list and all even nubmers in another list. store
##both list in a tuple and return   

def numbers(*t):
    
    even = [i for i in t if i % 2 == 0]
    odd = [i for i in t if i % 2 != 0]

    tup = (even,odd)

    return tup

t = (1,2,3,4,5,6,7,8,9)

print(f"The result will be {numbers(*t)}")