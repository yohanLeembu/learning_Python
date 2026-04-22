class pokemon:
    species = "Pokemon"

    def __init__(self, name, type, moves, personality): #constructor method(dunder method= double underscore method) with parameters
        self.name = name 
        self.type = type
        self.moves = moves
        self.personality = personality

    def attack(self):#method, a function an object does
        print(f"{self.name} attacked")

    def pokedex_check(self):
        print(f"{self.name} is {self.type} pokemon with these moves: {self.moves}")


