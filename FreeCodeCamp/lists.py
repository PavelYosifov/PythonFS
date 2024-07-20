mylst1 = ["Roger", 1, "Syd", True]

print("Roger" in mylst1) # checking if Roger is part of the list
print(mylst1[2]) # prints the 3rd variable
mylst1[2]= "Beau" # changing the 3rd variable from Syd to Beau
print(mylst1)
print(mylst1[-3]) # prints the 2nd variable, but it counts backwards
# ----------------------------------------------------------------
mylst2 = ["Roger", 1, "Syd", True, "Quincy", 7]
print(mylst2[2:4])  # slicing the list from 3rd argument to 4th
mylst2.append("Harry") # adds an argument to the list at the end of it
mylst2.extend(["Judah", 5]) # adds multiple arguments to the list
mylst2 += ["Judah", 5] # does the same thing as above
mylst2.insert(2, "Test") # inserts an argument to the list at the specified position
mylst2[1:1] = ["Test1", "Test2"] # inserts multiple arguments to the list at specified position
mylst2.remove("Judah") # removes an argument from the list
del mylst2[2] # removes an argument from the list based on their index
print(mylst2.pop()) # removes and prints the last argument from the list
print(len(mylst2)) # returns the length the list
# Sorting lists
mylst3 = ["Roger", "Syd", "Beau", "Quincy"]
mylst3copy = mylst3[:] # copies the list
mylst3.sort() # sorting the list in alphabetical order 
print(mylst3)
print(mylst3copy)
mylst3.append("bob")
mylst3.sort(key=str.lower) # sorting the list in alphabetical order and escaping Upper case first
print(sorted(mylst3, key=str.lower)) # printing and sorting the list without modifying it 
print(mylst3)