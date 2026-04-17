import random
print("==<<WELCOME TO TRYSTAL>>==")

print(("choose what you want to do:"))
print("1. Start Game")
print("2. Continue Game")
print("3. History")
print("4. Exit")
choice = input("Enter: ")


if choice == "1":
    pokemon_list = [
    {"name": "Pikachu", "hp": 35, "level": 10, "type": "Electric"},
    {"name": "Charmander", "hp": 39, "level": 12, "type": "Fire"},
    {"name": "Bulbasaur", "hp": 45, "level": 11, "type": "Grass"},
    {"name": "Squirtle", "hp": 44, "level": 13, "type": "Water"},
    {"name": "Jigglypuff", "hp": 115, "level": 8, "type": "Fairy"}
]
    def poke_list():
         poke_lists = []
         for pokemon in pokemon_list:
              poke_lists.append(pokemon["name"])
         return poke_lists
    def type_chart(attacker_type, defender_type):
        def effectiveness():
            # Super effective cases
            if (attacker_type == "Fire" and defender_type == "Grass") or \
            (attacker_type == "Water" and defender_type == "Fire") or \
            (attacker_type == "Grass" and defender_type == "Water") or \
            (attacker_type == "Electric" and defender_type == "Water"):
                print("Super effective!")
                return 20

            # Not very effective cases
            elif (attacker_type == "Fire" and defender_type == "Water") or \
                (attacker_type == "Water" and defender_type == "Grass") or \
                (attacker_type == "Grass" and defender_type == "Fire") or \
                (attacker_type == "Electric" and defender_type == "Grass"):
                print("Not very effective...")
                return 5

            # Normal damage
            else:
                return 10

        return effectiveness()


    opponent_poke = random.choice(pokemon_list)
    print(f"The opponent sends out {opponent_poke["name"]} !!!")



    print("Choose your Pokemon:")
    for i,poke in enumerate(poke_list(), start=1):
          print(f"{i}.{poke}")
    

    chosen_poke = input("Enter it's name: ")
    for pooke in pokemon_list:
        poke_no = pooke["name"]     
        if chosen_poke == poke_no:
            print(f"You chose {pooke["name"]}!!")
            break
    print(f"your pokemon:\n{pooke["name"]} lvl {pooke["level"]} \n(hp:{pooke["hp"]}) is on the battle")
    print(f"enemy:\n{opponent_poke['name']} lvl {opponent_poke["level"]} \n(hp:{opponent_poke["hp"]}) is on the battle")
    while True:
        print("Your move:")    
        print("1. Attack")
        action = int(input("enter your action: "))
        if action == 1:
            print(f"\n{pooke["name"]} has attacked {opponent_poke['name']}!!!")
            damage = type_chart(pooke["type"], opponent_poke["type"])
            print(f"attack did {damage} damage")
            opponent_poke["hp"] = opponent_poke["hp"] - damage
            print("hp:",pooke["hp"])
            input()
            print(f"\n{opponent_poke["name"]} has attacked {pooke['name']}!!!")
            opdmg = type_chart(opponent_poke["type"],pooke["type"])
            print(f"attack did {opdmg} damage")
            pooke["hp"] = pooke["hp"] - opdmg
            print("hp:",opponent_poke["hp"])

            if pooke["hp"] <= 0 or opponent_poke["hp"] <=0:
                break




    

    