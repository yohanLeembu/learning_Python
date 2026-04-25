from base import Player, enemy_list, enemies, encounter, Enemy
from colorama import Fore, Style
import time

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

if choose == 1:
      print("👑Dungeon Administrator: Good Luck! Adventurer")
      print("🔍 Exploring Dungeon...")

      time.sleep(2)

      enemy_encountered = encounter(name, enemies)
      full_hp = enemy_encountered.hp
      while name.hp >0 or enemy_encountered.hp >0:
            print("\nwhat will you do?")
            print(f"""
                  1. 🗡️ {Fore.RED}Fight{Style.RESET_ALL}
                  2. STATUS 📊 
                  3. CHECK INVENTORY 🎒
                  """)
            action = int(input("Choose: "))
            if action == 1:
                  print(name.attack(enemy_encountered))
                  time.sleep(1.5)
                  print("\n",enemy_encountered.attack(name))
                  time.sleep(1.5)



if choose == 4:
    enemy_list(enemies)
