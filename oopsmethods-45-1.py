##Define a class person with the instance object variables name and age. set instance object varialles in __init__() method. also define show() method to display
## name and age of the person

class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def show(self):
        print(f"The Age  of the person is {self.age}")
        print(f"The Name of the person is {self.name}")



age = int(input("Enter the age of yours::"))
name = input("Enter your name::")
e1 = person(age, name)
e1.show()





