##write  a python fucntion to calculate LCM of two numbers (TSRS)

def lcm(a,b):

    start = max(a,b)

    while True:
        if start % a == 0 and start % b == 0:
            return start
        
        start += 1

def main():

    a = int(input("Enter the 1st number::"))
    b = int(input("Enter the 2nd number::"))

    print(f"The lcm of {a} and {b} is {lcm(a,b)}")

main()

        
    

