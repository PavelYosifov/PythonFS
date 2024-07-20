def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ") # user input
    computer_choice= "paper"
    choices = {"player":player_choice, "computer":computer_choice} # dictionary!
    return choices
choices = get_choices()
print(choices)
#----------------------------------------------------------------
dog = {"name": "Roger", "age": 8} # dictionary with keys name and age and values Roger and 8
print(dog ["name"]) # prints the name Roger using its key value name
dog ["name"] = "Syd" # changes the name to "Syd"
print(dog ["name"]) # prints the name Syd using its key value name
print(dog) # prints the whole dictionary
print(dog.get("name")) # prints the name using the key name with get function
print(dog.get("color", "brown")) # prints the color using the key name with get function which was not present in the dictionary but .get created it.
print(dog.pop("name")) # prints the name using the key name with pop function and removes it from the dictionary
print(dog.popitem()) # prints the last key and value with popitem function and removes it from the dictionary
print("color" in dog) # checks if key color is present in the dictionary, will return True or False
print(dog.keys()) # prints all the keys in the dictionary
print(dog.values()) # prints all the values in the dictionary
print(dog.items()) # prints all the items in the dictionary
print(len(dog)) # prints the length of the dictionary
dog["favorite food"] = "Meat" # creates new pair of key and value
del dog ['color'] # deletes the color key and it's value from the dictionary