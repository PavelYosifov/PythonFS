import math
serial_name = str(input())
episode_duration = int(input())
break_duration = int(input())
time_left = break_duration - (break_duration / 8) - (break_duration / 4)
if time_left >= episode_duration:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(time_left - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(episode_duration - time_left)} more minutes.")
