##write a python fucntion to print all factors of given number

def factor(n):

    for i in range(1,n +1):

        if n % i == 0:
            print(i, end = " ")

n = int(input("Enter the number::"))
factor(n)