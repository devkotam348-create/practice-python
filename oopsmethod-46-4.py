##Define a class Accoutn with instance object variable balance with initial value as 0. Provide withdraw and deposit methods. Now define a subclass
##MinimumBalanceAccount of Account with provided miniumum balance. Override withdraw method according to minimum blalance condition

class Account:
    def __init__(self):
        self.balance = 0

    def withDraw(self,amt):
        if self.balance >= amt:
            self.balance = self.balance - amt
            print(f'you have {self.balance } left')
        else:
            print('You dont have enough balance')
    def Deposit(self, amt):
        self.balance = self.balance + amt
        print(f'your balance is ::{self.balance}')

class MinimumBalanceAccount(Account):
   def __init__(self, min):
       super().__init__()
       self.MinimumBalance = min
   def withDraw(self, amt):
       if self.balance - amt >= self.MinimumBalance: 
           self.balance = self.balance -amt
           print(f'You have {self.balance} left')
       else:
           print('You dont have enough money')
m = MinimumBalanceAccount(200)
m.Deposit(1000)
m.withDraw(300)
