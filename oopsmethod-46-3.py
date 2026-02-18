##Demostrate the use of super() in inheritence.

class apple():
    def __init__(self, weight):
        self.weight = weight

class amount(apple):
    def __init__(self, price,weight):
        super().__init__(weight)
        self.price = price

    def show(self):
        print(f'The total price of the apple is {self.weight * self.price}')


e = amount(100,2)
e.show()