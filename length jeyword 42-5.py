##write a fucntion which takes  variable length arguments to recieved an integers.  filter out the prime numbers and return the list of those prime numbers

def prime_num(*n):
    prime_list = []

    for a in n:
        if a <= 1:
            continue
        is_prime = True
        
        for d in range(2, int(a ** 0.5)+1):
            if a % d == 0:
                is_prime = False
                break
        else:
            prime_list.append(a)

    return prime_list



r = (1,2,3,4,5,6,7,8,9)
print(f"the list of prime numbers is {prime_num(*r)}")
