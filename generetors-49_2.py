###write a generator to produce squares of first n natural numbers.

def generate_square_number(n):
    
    for i in range(1,n+1):
        yield i ** 2
        

for i in generate_square_number(5):
    print(i, end =" ")
    
    
g = generate_square_number(4)
print(next(g))    
print(next(g))