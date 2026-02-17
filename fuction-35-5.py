## write a Python function to find all the common factors of two given numbers. Return a tuple of such factors(TSRS)

def comm(a,b):
    fact = []

    for i in range(1,min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            fact.append(i)

    return tuple(fact)

def main():
    a = int(input("Enter the 1st number::"))
    b = int(input("Enter the 2nd number::"))

    print(f"The common factors of {a} and {b} is {comm(a,b)}")

main()