#write a lambda expression to check if number is even

# f = lambda a: (a % 2 == 0)
# print("Even" if f(int(input("Enter the number::"))) else "not even")


a = int(input("Enter the number::"))
print("Even" if (lambda a: a% 2 == 0)(a) else "not even")