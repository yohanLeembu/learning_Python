# Learing about string, substring, and string manipulation
name = "Changli"

# string indexing
print(name[3]) #the letter that's index is 3
print(name[2]) 
print(name[-2])#hyphen index starts from -1 from the last letter

#string slicing
print(name[0:6:2])#format- string[starting index: ending index: steps], it alwayss shows string from left to right.
print(name[-4:-5:-1])#for negative indexing like this, steps are needed for system to slice to the left
print(name[0:])#from zero index to the end
print(name[-3:])#from -3 index to the right all
print(name[:5])#everything before the index 5

#substring
sub = name[0:6:1]#a part of a string is called substring 
print(sub)


#searching in string 
print("Cha" in name)
print("sdh" in name)


#find position
print(name.find("h"))#it is case sensitive
print(name.find("j"))#if the letter is not in the string, it shows -1


#String Splitting 
print(name.split("a"))
sentence = "I am Yohan"
print(sentence.split())
data = "pikachu,bulbasaur,charmander"
pokemon_list = data.split(",")
print(pokemon_list)

print(data.replace("pikachu", "squirtle"))#replacing strings in a string

print(name.replace("C", "i"))

#string maniputation imp
print(name[::-1]) #reversing a string
print(name.upper())  
print(name.lower())  
print(name.capitalize())

eg = "   plot  "
print(eg.strip())#removes spaces from both sides
print(eg.lstrip())#removes spaces from left (l = left)
print(eg.rstrip())#removes spaces from right (r = right)

#looping through string
for letter in name:
    print(letter)



#escape characters

print("Yohan\nlimbu") #after \n it prints from the next line
print("Name:\tYohan\nAge:\t20")#creates a tab space
print("Yohan\\pottery.com")#lets you write \
print("wow!! he said \"I Love You\"")#lets you write "" inside of ""
print('And She replied \'I love you too!\'')#lets you write '' inside of  ''

#multi line string, and is also used to explain the fuction for documentation
text = """Hello
This is line 2
This is line 3"""

print(text)#for multiline

def greet():#for explaining function
    """This function prints a greeting"""
    print("Hello")


#tuple and unpacking them (Unpacking = taking values out of a container into variables)
point = (10, 20, 30, 50, 70, 19)
person = ("Alice", 25, "Engineer")

name, age, job = person

print(name)

#Partial unpacking (* operator)
a, *middle, b = point
print(*middle)#prints whats in the middle of the first and the last
a, *rest = point#everything after the first


hui = {
    "name": "Yohan",
    "age": 13
}

#printing only the values
for i in hui.values():
    print(i)

#printing only the keys
for i in hui:
    print(i)

#printing both
for keys, values in hui.items():
    print(keys,":",values)


#Sets
nums = {1, 2, 3, 4, 5}#they are unordered, no indexing

change = sorted(nums)#converted to list to use index


#nested structure

data = {
    "users": [
        {"name": "Alice", "scores": (95, 88, 72)},
        {"name": "Bob",   "scores": (60, 75, 90)},
    ]
}

print(data["users"][1]["scores"][0])


