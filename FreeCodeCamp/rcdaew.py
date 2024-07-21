# recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(3))


# decorators
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")

    return wrapper


@logtime
def hello():
    print("hello")


hello()


# docstrings
def increment(n):
    """Increment a number."""
    return n + 1


print(help(increment))


# annotations
def increment(n: int) -> int:  # receives an integer and returns an integer
    return n + 1


count: int = 0

# exceptions
try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    result = 1
print(result)  # 1

try:
    raise Exception("An error!")
except Exception as error:
    print(error)

# with
filename = "Users/flavio/test/txt"
with open(filename, "r") as file:
    content = file.read()  # after reading the file it will automatically close it
    print(content)
