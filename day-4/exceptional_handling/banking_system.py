class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            if amount > self.balance:
                raise InsufficientFundsError("Insufficient funds in account.")
            self.balance -= amount
            return f"Withdrawal successful. Remaining balance: ₹{self.balance}"
        
        except ValueError as ve:
            return f"ValueError: {ve}"
        except InsufficientFundsError as ie:
            return f"InsufficientFundsError: {ie}"
        except Exception as e:
            return f"Unexpected Error: {str(e)}"


account = BankAccount(100)
print(account.withdraw(150)) 
print(account.withdraw(-10))
print(account.withdraw(50))  
