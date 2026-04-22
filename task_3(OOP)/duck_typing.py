# Duck typing = another way to achieve polymorphism besides inheritance
#                 object must have the minimum necessary attributes/methods
#                 "if it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dawg(Animal):
    def speak(self):
        print("Woof woof!!")

class MeowMeow(Animal):
    def speak(self):
        print("Me au, Me au~~")

class Car:#it meets the minimum necessary attributes and methods 
    alive = False
    def speak(self):
        print("Honk")

animals = [Dawg(), MeowMeow(), Car()] 
for animal in animals:
    animal.speak()
    print(animal.alive)