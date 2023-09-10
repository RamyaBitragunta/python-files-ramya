
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self,amount):
#         #self.balance = self.balance + amount #it can be ommited and can be written as
#         self.balance += amount
#
#     def withdraw(self,amount):
#         self.balance -= amount
#
#     def show_balance(self):
#         print("Balance is:",self.balance)
#
#
# account = BankAccount() #object creation
# account.deposit(1000)
# account.withdraw(499)
# account.show_balance()

# but in real life scenario - show balance should be private or authenticated
# there should be some mechanism how u will be aunthenticated by using username and password
# it cannot call show balance directly , first it should called if authentication true
# then only we wil show the balance
# if authentication is false then we will show nothing

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        #self.balance = self.balance + amount #it can be ommited and can be written as
        self.balance += amount

    def _withdraw(self,amount):
        self.balance -= amount

    def is_withdraw_Auth_True(self,isAuth_withdraw,amount):
        if isAuth_withdraw:
            print("You are Auth!, Withdraw")
            self._withdraw(amount)
        else:
            print("No auth, No Bal")

    def __show_balance(self):
        print("Balance is:",self.balance)

    def is_Auth_True(self,isAuth):
        if isAuth:
            print("You are Auth!")
            self.__show_balance()
        else:
            print("No Auth, No bal")


account = BankAccount() #object creation
account.deposit(1000)
account.is_withdraw_Auth_True(True,499)
account.is_Auth_True(True)
