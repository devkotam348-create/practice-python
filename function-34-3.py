##write a pyhon fuction to print all numbers between two given numbers(TSRN) 

def prime(a,b):

    num = a
    
    while num <= b:
        if num < 2:
            num += 1
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) +1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end = " ")

        num += 1

a = int (input("Enter the starting number::"))
b = int(input("Enter the last number::"))

prime(a,b)