from functools import reduce

t2 = lambda num: num * 2
print(t2(2))

multiply = lambda a, b: a * b
print(multiply(2, 4))

# map, filter and reduce functions
# map function
numbers = [1, 2, 3]


def double(a):
    return a * 2


result = map(double, numbers)
print(list(result))

# using lambda function, assigning it to "double"
double = lambda a: a * 2
result = map(double, numbers)
print(list(result))

# using only lambda function
result = map(lambda a: a * 2, numbers)
print(list(result))

# filter function
numbers2 = [1, 2, 3, 4, 5, 6]


def isEven(n):
    return n % 2 == 0  # even number checking


result = filter(isEven, numbers2)
print(list(result))
# using only lambda function
result = filter(lambda n: n % 2 == 0, numbers2)
print(list(result))

# reduce function
expenses = [
    ("Dinner", 80),
    ("Car repair", 120),
]
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)
