#composition = the composed object directly owns its components, which cannot exist independently 
#"owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power= horse_power



class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)] 

    def display_car(self):
        return f"{self.make} of {self.model} with {self.engine.horse_power} horse power and wheel size of {self.wheels[0].size}"

car1 = Car("Ford", "Mustang", 500, 18)

