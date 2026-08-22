class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def credit(self,amount):
        self.balance+=amount
        print("Account No =",B1.account_no)
        print("Balance Credited :", amount)
        print("Total Balance :",self.balance)


    def debit(self,amount):
        self.balance-=amount
        print("Balance Debited :", amount)
        print("Toatal Balance :",self.balance)

    def total_balance(self):
        return self.balance

B1=Account(5000,123456789)
B1.credit(5000)
B1.debit(500)
