import math
world_record = float(input())
distance = float(input())  # distance in meters
time_per_meter = float(input())  # time in seconds
resistance_time = math.floor(distance / 15) * 12.5
time_needed = (distance * time_per_meter) + resistance_time
if time_needed < world_record:
    print(f"Yes, he succeeded! The new world record is {time_needed:.2f} seconds.")
else:
    print(f"No, he failed! He was {(time_needed - world_record):.2f} seconds slower.")
