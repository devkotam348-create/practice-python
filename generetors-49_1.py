###wrtite a generator to produce first n prime numbers.

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def generate_prime_number(n):
    count = 0
    x = 2
    while count < n:
        if is_prime(x):
            yield x
            count += 1
        x += 1
        

for i in generate_prime_number(10):
    print(i, end=' ')
    
    
    
    
    
    
   