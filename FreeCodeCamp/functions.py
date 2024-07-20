def hello():
    print("Hello!")
hello(); hello(); hello() # 3 lines on the same line

def hello1(name = "my friend"):
   print("Hello, " + name)
hello1("Pavel"); hello1("Quincy")
hello1() # we call the function without any parameters but it will display my friend by default

def hello2(name, age):
   print("Hello, " + name + ", you are " + str(age) + " years old.") # str(age) is for declaring age as string
hello2("Pavel", 24)

# creating a function with a return in it
def hello3(name):
    if not name:
        return
    print("Hello, " + name + "!")
hello3("Beau")

# creating a function with a return that will return the values plus the name we gave in the function
def hello4(name):
    print("Hello, " + name + "!")
    return name, "Beau", 8
print(hello4("Syd"))

# Variable scope
age = 9 # global variable
def test():
    age = 8 # local variable
    print(age)
print(age) # 9
test() # 8

# Nested functions
def talk(phrase):
    def say(word): # nested function
        print(word)
    words = phrase.split(" ") # create a list of words
    for word in words: # for loop for each word
        say(word)
talk("I am going to buy the milk")

def counter():
    count = 0 # setting the count to zero
    def increment(): # nested function
        nonlocal count # using nonlocal keyword to modify the count variable
        count += 1
        return count # return the number of count
    return increment # return the increment of the counter
increment = counter() # this way we can increment the counter
print(increment()) #1
print(increment()) #2
print(increment()) #3