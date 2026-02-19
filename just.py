class Bank:
    bank_name = "Global Bank"     # class variable
    total_accounts = 0            # class variable

    def __init__(self, owner, balance):
        self.owner = owner        # instance variable
        self.balance = balance    # instance variable
        Bank.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    @staticmethod
    def validate_amount(amount):
        return amount > 0


b1 = Bank("Alice", 1000)
b2 = Bank("Bob", 2000)

print(Bank.total_accounts)
