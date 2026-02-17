##write a python function to create a list of prime numbers between two given numbers(TSRS)

def prime(a,b):

    p = []
    num = a
   
    
    while num <= b:
            is_prime = True
            if num < 2:
                num += 1
                continue

            for i in range(2, int(num**0.5)+ 1):
                if num % i == 0:
                    is_prime= False
                    break

            if is_prime:
                p.append(num)

            num += 1

    return p


def main():

    a = int(input("Enter the 1st number::"))
    b = int(input("Enter the 2nd number"))

    print(f"The list of prime number between the two number are {prime(a,b)}")


main()