##define a class person with instance objcet variable name and age. Provide __int__method to set instace object variablle allso define method to show 
##name and age. Now define a subclass Employee  of person with instant object 


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showName(self):
        print(f"Name: {self.name} \nAge: {self.age}")
class employee(person):
    def __init__(self,name, age, salary ):
          self.salary = salary
          super().__init__(name,age)
      
    def showName(self):
        super().showName()
        print(f"Salray:{self.salary}")

name = input("Enter the name::")
age = int(input('Enter the age::'))
salary = int(input('Enter the salary::'))
e = employee(name, age, salary)
e.showName()
