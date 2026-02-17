##Define a class team with instace object variable a list of team member names. Provides method to input member names and displlay member names.

class team:
    def __init__(self):
        self.members = []
    
    def addmembers(self, name):
        self.members.append(name)
    def printmembers(self):
        print(self.members)

t = team()
count = int(input('How many team mebers you want to add::'))

for i in range(count):
      name = input("Enter member name::")
      t.addmembers(name)
t.printmembers()
