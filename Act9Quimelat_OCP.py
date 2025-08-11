class Role:
    def get_access(self):
        return "No access"

class Admin(Role):
    def get_access(self):
        return "Full access"

class Editor(Role):
    def get_access(self):
        return "Can edit"

class Remover(Role):
    def get_access(self):
        return "Can remove"

class Viewer(Role):
    def get_access(self):
        return "Can view"
    
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def access(self):
        return self.role.get_access()
    
print(User("Alice", Admin()).access())
print(User("Bob", Viewer()).access())
print(User("Jack", Remover()).access())