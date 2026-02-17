#Write a lambda finction to find out the hcf 

f = lambda a,b: max(i for i in range(1, min(a,b)+1) if a % i == 0 and b % i == 0)

print(f(2,4))

