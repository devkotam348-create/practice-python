##write a function to check if the given sides of triangle can form a valid triangle or not. Define decorator t0 print "Right angled triangle" if the triangle is right
##angled triangle 

def main(func):
       def wrapper(a,b,c):
              if func(a,b,c) == True:
                   if a > b and a > c:
                        if a**2 == b**2 + c**2:
                              print("is right angled triangle")
                        else:
                              print("is not right angles triangle")
                   elif b > a and b > c:
                         if b**2 == a**2 + c**2:
                              print("is right angled triangle")
                         else:
                              print("is not right angles triangle")
                   else: 
                         if c**2 == a**2 + b**2:
                               print("is right angled triangle")
                         else:
                              print("is not right angles triangle")
              
       return wrapper
                          






@main
def angle(a,b,c):
       is_triangle = True
       if a + b > c and a + c > b and b + c > a:
              return True
       else:
              return False
              

a = 45
b = 25
c = 35
angle(a,b,c)
