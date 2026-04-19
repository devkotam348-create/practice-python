#reverse a number
def Count(n, reverse = 0):
    if n == 0:
        return reverse
    return Count(n//10, reverse*10 + (n%10))
    
n = 121

result = Count(121)
if result == n:
    print("is palidrome")
else:
    print("is not palidrome")
