name = "Pavel"
age = 26
is_logged_in = True
favorite_food = ["Pizza", "Orizonki", "Crackers", "Popcorn"]
print("User: ", name)
print("Age: ", age)
print("Is the user logged in: ", is_logged_in)
# This way on the console the list will be displayed like Pizza, Orizonki, Crackers, Popcorn
print("Favorite food: ", ", ".join(favorite_food))

person = {"name": "Pavel", "age": 26, "hobbies": ["football", "basketball", "skiing"]}
print("Name:", person["name"])
print("Age:", person["age"])
# This way on the console the list will be displayed like football, basketball, skiing
print("Hobbies:", ", ".join(person["hobbies"]))
