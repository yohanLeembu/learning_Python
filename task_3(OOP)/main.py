
from pokemons import pokemon

pikachu = pokemon("Pikachu", "Electric", "Electro Ball, Iron Tail, Quick Attack, Thunder", "Hasty")
charizard = pokemon("Charizard", "Fire/Flying", "Flamethrower, Fly, Dragon Claw, Slash", "Brave")
bulbasaur = pokemon("Bulbasaur", "Grass/Poison", "Vine Whip, Razor Leaf, Sleep Powder, Solar Beam", "Calm")
squirtle = pokemon("Squirtle", "Water", "Water Gun, Bubble, Aqua Tail, Rapid Spin", "Relaxed")
gengar = pokemon("Gengar", "Ghost/Poison", "Shadow Ball, Dark Pulse, Hypnosis, Dream Eater", "Timid")
lucario = pokemon("Lucario", "Fighting/Steel", "Aura Sphere, Close Combat, Extreme Speed, Metal Claw", "Serious")

print(pikachu)#prints out the memory address
print(pikachu.moves)

pikachu.attack()#calling a method

charizard.pokedex_check()

print(pikachu.species)

print(pokemon.no_pokemon)