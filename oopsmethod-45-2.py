##Define a class circle with an instance object variable radius.  Provide setter and getter form the for radius. Also define GetArea() and 
## Getcircumference()methods.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def SetRadius(self, radius):
        self.radius = radius
    def GetRadius(self):
        return self.radius
    def GetArea(self):
        return math.pi * self.radius**2
    def GetCircumferemce(self):
        return 2*math.pi*self.radius
    
c = Circle(5)

print(c.GetRadius())
print(c.GetArea())
c.radius = 10
print(c.GetRadius())
c.SetRadius(10)
print(c.SetRadius(12))
