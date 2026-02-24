##define a funtion to find greater value among three given data. Handle all possible exceptions

def greatest(a,b,c):
    if (a==b or a == c) or ( c == b):
        raise ValueError("same number repeated (duplicates are not allowed)")
      
     
    if a >b and a >c:
        return a
    elif b > c and b >a:
        return b
    else:
        return c

try:
        a = int(input('Enter number for a::'))
        b = int(input('Enter number for b::'))
        c = int(input('Enter number for c::'))
        
        x = greatest(a,b,c)
        print(f'{x} is the greatest number')
        
except ValueError as e:
    print(e)



print('program contines....')

