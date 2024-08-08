firstname = str(input())
lastname = str(input())
age = int(input())
town = str(input())
# print(f"You are {firstname} {lastname}, a {age}-years old person from {town}.")
print(
    "You are "
    + firstname
    + " "
    + lastname
    + ", a {}".format(age)
    + "-years old person from "
    + town
    + "."
)
