holiday_price = float(input())
puzzle_quantity = int(input())
doll_quantity = int(input())
bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())
discount = 0
difference = 0
total_quantity = puzzle_quantity + doll_quantity + \
    bear_quantity + minion_quantity + truck_quantity
total_price = (puzzle_quantity * 2.6) + (doll_quantity * 3) + \
    (bear_quantity * 4.10) + (minion_quantity * 8.2) + (truck_quantity * 2)
if total_quantity >= 50:
    discount = 0.25 * total_price
    total_price -= discount
money_left = total_price - (total_price * 0.1)
if money_left >= holiday_price:
    difference = money_left - holiday_price
    # "{:.2f}".format(difference) or difference:.2f} round the number to the second symbol after the comma
    print(f"Yes! {difference:.2f} lv left.")
else:
    difference = holiday_price - money_left
    print(f"Not enough money! {difference:.2f} lv needed.")
