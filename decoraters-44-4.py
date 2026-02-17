###write a function to check if a given number N is a prime or not. define a decorator to print total numbers of prime numbers  before N 
def prime(func):
    def wrapper(n):
        if func(n) == True:
            print(f"{n} is the prime number::")
        else:
            print(f"{n} is the not prime number::")

        count = 0

        for i in range(2,n):
            if func(i) == True:
                count += 1

        print(f"There are {count} prime number before {n} ")
    return wrapper


        
        
            

@prime
def prime_num(n):
    is_prime = True
    for i in range (2, int(n ** 0.5)+1):
        if n % i == 0:
            is_prime = False
            return False
    if is_prime:
        return True
    
n = int(input("Enter the number you want to check the number is prime or not::"))
prime_num(n)