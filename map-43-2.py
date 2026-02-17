##write a python script to find number of digits in each of the element in a given tuple of number. Use map fucntion

t = (1,2,3,1,2,4,5,6,2)
print (list(map(lambda x: len(str(x)),t)))