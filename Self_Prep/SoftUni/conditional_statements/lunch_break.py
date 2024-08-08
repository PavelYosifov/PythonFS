budget = float(input())
gpu_qt = int(input())
cpu_qt = int(input())
ram_qt = int(input())
gpu_price = gpu_qt * 250
cpu_price = (gpu_price * 0.35) * cpu_qt
ram_price = (gpu_price * 0.10) * ram_qt
total_price = gpu_price + cpu_price + ram_price
if gpu_qt > cpu_qt:
    total_price = total_price - (total_price * 0.15)
if budget >= total_price:
    print(f"You have {(budget - total_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_price - budget):.2f} leva more!")
