##Use iter and next method to check if all the elements of a list are even numbers using while loop which should work equivalent to for loop

a = [2,4,6,8]

li = iter(a)
is_even = True

while True:
    try:
        b = next(li)
        if b % 2 != 0:
            is_even = False
            print('No not all elemets in list is even')
            break
    
    except StopIteration:
        break
if is_even:
    print('All the elements in list is even')