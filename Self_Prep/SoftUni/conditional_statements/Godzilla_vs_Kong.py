budget = float(input())
actors = int(input())
clothing_price = float(input())
decor_price = 0.1 * budget
if actors > 150:
    clothing_price = clothing_price - (clothing_price * 0.1)

total_cost = decor_price + clothing_price * actors
if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")
