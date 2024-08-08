hour = int(input())
minutes = int(input())
minutes += 15
if minutes >= 60:
    minutes -= 60
    hour += 1

if hour >= 24:
    hour -= 24

print(f"{hour}:{minutes:02d}")  # minutes are always displayed in two digits using :02d
