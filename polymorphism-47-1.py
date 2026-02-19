##define a Python clss Person with name and age as instance object variables. Define Student and Teacher tow subclasses of PErson., Provide rollNo as instance 
##object variable in Student, provide subject as instace object variable in Teacher class. Now define a function show to print values of instancce object variables in 
###both the classes. Demonstrate polymophic behaviour or show function


class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, rollNo, name, age):
        self.rollNo = rollNo
        super().__init__(name, age)

    def show(self):
        print(f'The name of the student is {self.name} and age is {self.age} and roll number is {self.rollNo}')

class Teacher(Person):
    def __init__(self, Subject,name,age):
        self.Subject = Subject
        super().__init__(name,age)
    def show(self):
        print(f'The name of the Teacher is {self.name} and his age is {self.age} and teaches {self.Subject}' )


a = Student(5,'mahendra', 22)
a.show()




