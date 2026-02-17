##write a python script to create a list of numbers greater than a given number N(taken form the user ) for ean element in a given set of numbers. use filter function.

s = {1,2,3,4,5,6,7,8,9}

n = int(input("Enter you desire number to start after::"))

print(list(filter(lambda x:  x > n, s )))