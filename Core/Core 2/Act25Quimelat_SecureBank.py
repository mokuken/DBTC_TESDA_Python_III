class BankAccount:
    def __init__(self, name, initial_balance, branch):
        self.name = name                  # Public attribute
        self.__balance = initial_balance  # Private attribute
        self._branch = branch             # Protected attribute

    # Public method to view account holder's name
    def get_name(self):
        return self.name

    # Public method to deposit money safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money safely
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    # Public method to check balance (read-only access)
    def get_balance(self):
        return self.__balance

    # Protected method to access branch info (used internally or by subclasses)
    def _get_branch(self):
        return self._branch


account = BankAccount("Alice", 1000, "Downtown Branch")
print(account.get_name())   
account.deposit(500)        
account.withdraw(200)       
print(account.get_balance())
