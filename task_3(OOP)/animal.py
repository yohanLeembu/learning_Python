class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("bark!")

class Meg(Animal):
    def speak(self):
        print("Roar!!")

class Zebra(Animal):
    def speak(self):
        print("Jeep!!")

dog = Dog("Brian")

meg = Meg("Shark")

zebra = Zebra("Marty")

print(dog.name)
print(zebra.isAlive)
meg.sleep()


dog.speak()
meg.speak()
zebra.speak()