##Define a class rectangle with the length and breadth as instance object provide setDimension(), showDimension() and getArea() method in it

class rectangle:
    def __init__(self, length, breadth):
        if length < 0 or breadth <0:
            raise ValueError("Length and breadth must be greater than 0")
        self.length = length
        self.breadth = breadth 
    def setDimension(self, length, breadth):
        if length < 0 or breadth <0:
            raise ValueError("Length and breadth must be greater than 0")
        self.length = length
        self.breadth = breadth
    def showDimension(self):
        return self.length, self.breadth
    def getArea (self):
        return self.length * self.breadth


while True:
    try: 
        l = float(input("Enter length::"))
        b = float(input("Enter breadth::"))
        r = rectangle(l,b)
        break
    except ValueError as e:
        print("Invalid input::", e)
print("Dimension::",r.showDimension() )
print("Area::",r.getArea())
            
        
    