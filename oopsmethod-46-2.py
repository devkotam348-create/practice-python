##Define a class Account with instance object variables accountNo, balance and static variable rate_of_interest. Provide needful metho0ds. Define subclass Fixed 
##of account class with instance object variable time. Provide setter and getter. Also define a method to calculate simple intrest

class Account:

    rate_of_intrest = 5
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance

class Fixed(Account):
    def __init__(self,accountNo,balance,time):
       super().__init__(accountNo, balance)
       self.time = time
    
    def setTime(self,time):
        self.time = time
    
    def getTime(self):
        return self.time
    
    def simpleIntrest(self):
         return (self.balance * self.time * self.rate_of_intrest)/100
    


accountNo = int(input('Enter the Account Number::'))
balance = int(input("Enter the balance you have::"))
time = int(input('Enter the time::'))
e1 = Fixed(accountNo, balance, time)
print(f'The intrest is {e1.simpleIntrest()}')

new_time = int(input('Enter you new time::'))

e1.setTime(new_time)

print(f'The updated intrest is : {e1.simpleIntrest()}')
         


