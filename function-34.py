#write a funciton python to print first n prime numbers (TSRN)

def prime(n):
    count = 0
    num = 2

    while count < n:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end = " ")
            count += 1

        num += 1

n = int(input("Enter how many prime number you want to print::"))
prime(n)
 