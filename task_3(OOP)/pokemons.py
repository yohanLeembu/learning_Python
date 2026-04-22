class pokemon:
    species = "Pokemon"#class varaible, every object can access it
    no_pokemon = 0
    def __init__(self, name, type, moves, personality): #constructor method(dunder method= double underscore method) with parameters
        self.name = name #instance varaible
        self.type = type
        self.moves = moves
        self.personality = personality
        pokemon.no_pokemon += 1

    def attack(self):#method, a function an object does
        print(f"{self.name} attacked")

    def pokedex_check(self):
        print(f"{self.name} is {self.type} pokemon with these moves: {self.moves}")


