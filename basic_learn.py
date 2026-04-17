##working with variables
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# nxtyr_age = age + 1

# print(f"hello {name}, you are gonna be {nxtyr_age} years old, the following year")


#working with data types
# hin = True
# ben = int(input("enter the age of ben: "))

# ben = 2 * ben

# if ben <= 5:
#     hin = False
#     print(ben)
    
# print(hin)

#working wiht arrays

# shopping_list = []

# # Add items
# for i in range(3):
#     item = input("Enter an item you want to buy: ")
#     shopping_list.append(item)

# Print list nicely
# print("\nThese are your items:")
# for item in shopping_list:
#     print(f"- {item}")

# # Remove item safely
# while True:
#     remove_item = input("\nEnter the item you want to remove: ")

#     if remove_item in shopping_list:
#         shopping_list.remove(remove_item)
#         print(f"{remove_item} removed successfully.")
#         break
#     else:
#         print("Item not found in the list.")

# # Final list
# print("\nUpdated shopping list:")
# for item in shopping_list:
#     print(f"- {item}")

print("\n=== Dino Game ===\n")

player_name = input("enter your name player: ")
print(f"welcome to the game Player {player_name}")
Dinos = []
n = int(input("enter the number of dino you want to add: "))

for i in range(1,n+1):
    name = input(f"Enter the name of dino {i}: ")
    age = float(input("Enter its age: "))
    weight = float(input("Enter its weight: "))
    danger = input("is it dangerous(y/n): ")


    Dinos.append({
        "name": name,
        "age" : age,
        "weight" : weight,
        "danger" : danger
    })

print("list of dinos: ")
for i,dino in enumerate(Dinos, start=1):
    print(f"{i}. {dino['name']} - Age: {dino['age']}, Weight: {dino['weight']}, Danger: {dino["danger"]}")


option = input("do you wanna add or remove the dino(add/remove/nothing): ").lower()

if option == "add":
    for i in range(1,n+1):
        name = input(f"Enter the name of dino {i}: ")
        age = float(input("Enter its age: "))
        weight = float(input("Enter its weight: "))
        danger = input("is it dangerous(y/n): ")


        Dinos.append({
            "name": name,
            "age" : age,
            "weight" : weight,
            "danger" : danger
            })

elif option == "remove":
    remove_dino = input("enter the dino name:").lower()
    for dino in Dinos:
        if dino["name"].lower() == remove_dino:
            Dinos.remove(dino)
            print("Dino removed successfully.")
            print(Dinos)
            break
        else:
            print("Dino not found.")
else:
    print("!"*100)

timeskip = int(input("enter the timeskip days: "))

for dino in Dinos:
    dino["age"] += timeskip / 365

print("list of dinos: ")
for i,dino in enumerate(Dinos, start=1):
    print(f"{i}. {dino['name']} - Age: {round(dino['age'], 2)}, Weight: {dino['weight']}, Danger: {dino["danger"]}")