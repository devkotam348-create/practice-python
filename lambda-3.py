#write a lambda expression to calculate the area of the circle
import math
r = int(input("Enter the radius::"))

print(f"Ther are of the circle is {(lambda a:a**2 * math.pi)(r)}")