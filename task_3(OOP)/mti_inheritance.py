#multiple ineritance = Child(Parent1, Parent2)
#multi-level ineritance = A -> B(A) -> C(B)

class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print("I am running btch, ahhhh!!!!")

class Predator(Animal):
    def hunt(self):
        print("Yeah! I am gonna get ya hehehe~~")


class Rabbit(Prey):
    pass

class Wolf(Predator):
    pass

class Human(Prey, Predator):
    pass

rabbit = Rabbit("Rabbit")
wolf = Wolf("Wolf")
human = Human("Human")

wolf.hunt()
human.flee()
wolf.eat()