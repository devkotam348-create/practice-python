###1. write a recursive funtion to calculate sum of first N natural numbers.
# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)

# print(sum(5))

##2. write a fucntion to calculate sum of first N odd natural numbers

# def odd(n):
#     if n == 0:
#         return 0
#     return odd(n-1) + (2*n-1)

# print(odd(5))
##3. write a recursive function to claculate sum of first N even natural number
# def even(n):
#     if n == 0:
#         return 0
#     return even(n-1) + 2*n

# print(even(5))

##4. write a recursive fuction to calculate factorial of a number

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

##5. write a recursive funtion to calculate sum of squares of first N natural numbers
def squares(n):
    if n == 0:
        return 0
    return n**2 + squares(n-1)

print(squares(2))