##Define a class Polygon with instance object variable to store number of sides and list of n side length values. Define a 
# subclass Trangel of Polygon with instance methods getArea()

class Polygon:
    def __init__(self,sides):
        self.n = len(sides)
        self.sides = sides 

class Triangle(Polygon):
    def __init__(self, sides):
        super().__init__(sides)
        if self.n != 3:
                raise ValueError("Ther triangle polygon must contain 3 sides:::")
   
    def getArea(self):
         a = self.sides[0]
         b = self.sides[1]
         c = self.sides[2]
         
         s = (a+b+c)/2

         area = (s * (s -a) * (s-b) * (s-c)) ** 0.5
         return area



         
    