###write a function to calculate HCF of two numbers. define decorator for HCF function to tell whether the numbers are co-prime or not.

def function (func):
    def wrapper(a,b):
        a = func(a,b)
        if (a == 1):
            print('is co-prime numbers')
        else: 
            print('is not co-prime numbers')

    return wrapper


@function
def hcf(a,b):
    while b!= 0:
        a, b = b, a% b
    return a


print(hcf(6,8))