###Create a class employee with attributes empid, naem, salary and also define method to access properties of employee..


class Employee:
    def __init__(self, empid,name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    
    def setEmpid(self,empid):
        self.empid = empid
    def setName(self,name):
        self.name = name
    def setSalary(self,salary):
        self.salary = salary
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalry(self):
        return self.salary

#t1 = Employee(203,'Mahendra', 5000)
t2 = Employee()
t2.setEmpid(2003)
t2.setName('Dinesh')
t2.setSalary(50000)
print(t2.getEmpid(), t2.getName(), t2.getSalry())
print(t1.getEmpid(), t1.getName(), t1.getSalry())
