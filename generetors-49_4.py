##Use iter and next method to print vlaues of a given list using while loop which works equivalnet to for loop.

a = [2,4,6,7,8,9]

it = iter(a)
while True:
    try:
        print(next(it), end = ' ')
    except StopIteration:
        break


