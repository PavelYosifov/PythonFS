names = ("Roger", "Syd", "Beau")
print(names[0])  # returns the name of the variable on that index
print(names.index("Roger"))  # returns the index of the variable
print(len(names))  # returns the length of the tuple
print("Roger" in names)  # prints if Roger is part of the tuple or not
print(names[0:2])  # extracts and prints part of the tuple
sorted(names)  # sorts the tuple but will not modify the tuple itself
newtuple = names + ("Tina", "Quincy")  # concatenates the new tuple with tuple names
