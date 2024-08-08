import math

figure = str(input())
if figure == "square":
    a = float(input())
    area = a**2  # power of 2
    print(round(area, 3))
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(round(area, 3))
elif figure == "circle":
    radius = float(input())
    area = math.pi * (radius**2)  ## power of 2 and importing p from math
    print(round(area, 3))
elif figure == "triangle":
    a = float(input())
    ha = float(input())
    area = (a * ha) / 2
    print(round(area, 3))
else:
    print("Invalid figure!")
