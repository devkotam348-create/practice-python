##write a python script to filter only int type values in a given list of elelments. Use filter function 

a = [1,2,'3', 'mah',4,'5']

print(list(filter(lambda x : type(x)== int,a)))