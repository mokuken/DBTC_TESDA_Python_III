class Transporation:
    def move(self):
        return "Transport a to b"
    
class Car(Transporation):
    def move(self):
        return "the car moves a to b"

class Bicycle(Transporation):
    def move(self):
        return "the bicycle moves a to b"
    
def start_movement(transporation):
    print(transporation.move())

car = Car()
bicycle = Bicycle()

start_movement(car)
start_movement(bicycle)
