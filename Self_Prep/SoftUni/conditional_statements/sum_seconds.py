import math

first_time = int(input())
second_time = int(input())
third_time = int(input())
total_time = first_time + second_time + third_time
minutes = total_time // 60  # calculate minutes
math.floor(minutes)  # floor minutes
seconds = total_time % 60  # calculate seconds
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
