import random
import time

# -------------------- DATA --------------------
pokemon_list = [
    {"name": "Pikachu", "hp": 35, "level": 10, "type": "Electric"},
    {"name": "Charmander", "hp": 39, "level": 12, "type": "Fire"},
    {"name": "Bulbasaur", "hp": 45, "level": 11, "type": "Grass"},
    {"name": "Squirtle", "hp": 44, "level": 13, "type": "Water"},
    {"name": "Jigglypuff", "hp": 115, "level": 8, "type": "Fairy"}
]

# -------------------- MENU --------------------
def display_menu():
    print("==<<WELCOME TO TRYSTAL>>==")
    print("1. Start Game")
    print("2. Exit")
    return input("Enter: ")


# -------------------- SELECTION --------------------
def choose_pokemon(pokemon_list):
    print("\nChoose your Pokémon:")
    for i, poke in enumerate(pokemon_list, start=1):
        print(f"{i}. {poke['name']}")

    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(pokemon_list):
                selected = pokemon_list[choice - 1].copy()
                print(f"\nYou chose {selected['name']}!")
                return selected
            else:
                print("Invalid choice.")
        except:
            print("Enter a valid number.")


def get_random_opponent(pokemon_list, player):
    opponent = random.choice(pokemon_list)
    while opponent["name"] == player["name"]:
        opponent = random.choice(pokemon_list)

    opponent = opponent.copy()
    print(f"\nOpponent sends out {opponent['name']}!")
    return opponent


# -------------------- BATTLE LOGIC --------------------
def type_chart(attacker_type, defender_type):
    if (attacker_type == "Fire" and defender_type == "Grass") or \
       (attacker_type == "Water" and defender_type == "Fire") or \
       (attacker_type == "Grass" and defender_type == "Water") or \
       (attacker_type == "Electric" and defender_type == "Water"):
        print("Super effective!")
        return 20

    elif (attacker_type == "Fire" and defender_type == "Water") or \
         (attacker_type == "Water" and defender_type == "Grass") or \
         (attacker_type == "Grass" and defender_type == "Fire") or \
         (attacker_type == "Electric" and defender_type == "Grass"):
        print("Not very effective...")
        return 5

    else:
        return 10


def attack(attacker, defender):
    print(f"\n{attacker['name']} attacks {defender['name']}!")
    damage = type_chart(attacker["type"], defender["type"])
    print(f"Damage: {damage}")

    defender["hp"] -= damage   # ✅ augmented assignment

    if defender["hp"] < 0:
        defender["hp"] = 0


def display_status(player, opponent):
    print("\n--- STATUS ---")
    print(f"{player['name']} (HP: {player['hp']})")
    print(f"{opponent['name']} (HP: {opponent['hp']})")


def battle(player, opponent):
    print("\n--- BATTLE START ---")

    while True:
        display_status(player, opponent)

        # Player turn
        input("\nPress Enter to attack...")
        attack(player, opponent)

        if opponent["hp"] <= 0:
            print(f"\n{opponent['name']} fainted!")
            print("🎉 You win!")
            break

        time.sleep(1)

        # Opponent turn
        attack(opponent, player)

        if player["hp"] <= 0:
            print(f"\n{player['name']} fainted!")
            print("💀 You lose!")
            break

        time.sleep(1)


# -------------------- MAIN LOOP --------------------
while True:
    choice = display_menu()

    if choice == "1":
        player = choose_pokemon(pokemon_list)
        opponent = get_random_opponent(pokemon_list, player)
        battle(player, opponent)

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")