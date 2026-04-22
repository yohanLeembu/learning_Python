# Abstract class cannot be instatiated on its own, its meant to be subclassed.
#they can contain abstract methods, which are declared but have no implementation.
#Abstract classes benefits:
#1. prevents instantiation of the class itself
#2. requires children to use inherited class methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(slef):
        pass

class Car(Vehicle):
    def go(self):
        print("drive the car")

    def stop(slef):
        print("stop the car")

class MoterBike(Vehicle):
    def go(self):
        print("Drive the Bike")

    def stop(slef):
        print("stop the Bike")


#{class Boat(Vehicle): this class wont be able to instantiated and run 
#    def go(self):     because it didn't define both bethods in the abstract class
#       print("Boat is sailing")} abstract class works like a checklist  or a rule that a class mush make both of these methods

car = Car()
motorBike = MoterBike()

car.go()
motorBike.stop()
