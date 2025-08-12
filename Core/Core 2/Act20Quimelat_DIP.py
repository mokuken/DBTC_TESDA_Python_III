# Abstact Class
class Supplier:
    def get_beans(self):
        raise NotImplementedError("Supplier must implement get_beans()")

# Low-level classes
class FarmerJuan(Supplier):
    def get_beans(self):
        print("Get the beans from Juan")

class FarmerWoo(Supplier):
    def get_beans(self):
        print("Get the beans from Woo")

# High-level classes
class CoffeeShop:
    def __init__(self, supplier):
        self.supplier = supplier

    def serve_coffee(self):
        self.supplier.get_beans()

juan = FarmerJuan()
woo = FarmerWoo()

supply = CoffeeShop(juan)
supply.serve_coffee()
