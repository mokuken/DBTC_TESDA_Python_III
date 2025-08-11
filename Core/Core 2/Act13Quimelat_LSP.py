# Liskov Substitution Principle (LSP) Example
class PaymentMethod:
    def pay(self, amount):
        print("paying ", amount)

# This class adheres to LSP and implements the pay method correctly.
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print("Transferring", amount, "via Bank Transfer.")

# This class violates LSP because it does not implement the pay method safely.
# class CashPayment(PaymentMethod):
#     def pay(self, amount):
#         raise Exception("Cash payment is not safe.")

# This class is a safe version of CashPayment that adheres to LSP.
class SafeCashPayment(PaymentMethod):
    def pay(self, amount):
        print("Safe paying", amount)

# The process_payment function should accept any subclass of PaymentMethod.
def process_payment(payment: PaymentMethod, amount):
    payment.pay(amount)

# Example usage:
process_payment(BankTransfer(), 5000)
# process_payment(CashPayment(), 100)
process_payment(SafeCashPayment(), 1500)
