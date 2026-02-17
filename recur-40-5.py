##write a recursive function to calculate sum of first N Prime numbers.

def is_prime(n, d=2):
    if n < 2:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)

def sum_primes(n, current=2):
    if n == 0:
        return 0

    if is_prime(current):
        return current + sum_primes(n - 1, current + 1)
    else:
        return sum_primes(n, current + 1)

r = int(input("Enter how many primes you want to sum: "))
print(f"Sum of first {r} prime numbers is {sum_primes(r)}")
