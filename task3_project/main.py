from base import Player, enemy_list, enemies
from colorama import Fore, Style

print("🐉⚔️ WELCOME TO THE EXTRAORDINARY DUNGEON⚔️🐉")

print("Name your Character")
name = input("Enter Your Name: ")
print(f"👑Dungeon Administrator: oh! Your name is {name}. Quite the quirky name you have, Adventurer🧭")
name = Player(name)


print(f"""
👑Dungeon Administrator: CHOOSE YOUR DECISION!
      1. EXPLORE DUNGEON 🗡️ {Fore.RED}Fight{Style.RESET_ALL}
      2. CHECK STATUS 📊 
      3. CHECK INVENTORY 🎒
      4. ENEMY INFO 👹
      5. EXIT DUNGEON 👋
""")

choose = int(input("enter the number: "))

if choose == 4:
    enemy_list(enemies)
