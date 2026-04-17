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
print("Name:\tYohan\nAge:\t20")
print("Yohan\\pottery.com")
print("wow!! he said \"I Love You\"")
print('And She replied \'I love you too!\'')