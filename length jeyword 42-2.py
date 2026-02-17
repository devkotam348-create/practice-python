##write a function which receives variable length arguments to find greatest element. it return the greatest element

def greatest(*t):
    return max(*t)

t = (1,2,5,8,12,35,9,8)
print(f"The max number in the given is {greatest(*t)}")