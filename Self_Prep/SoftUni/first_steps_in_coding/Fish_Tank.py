length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100
volume = (length * width * height) * 0.001 # converting volume from cubic decimeters to liters 
water_needed = volume * (1 - percent)
print(water_needed)
