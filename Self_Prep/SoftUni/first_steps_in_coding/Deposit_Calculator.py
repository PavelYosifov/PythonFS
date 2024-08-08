deposit = float(input())
period = int(input())
percent = float(input()) / 100 # We want percentage, so whatever number we type we must divide it by 100
sum = deposit + period * ((deposit * percent) / 12)
print(sum)
