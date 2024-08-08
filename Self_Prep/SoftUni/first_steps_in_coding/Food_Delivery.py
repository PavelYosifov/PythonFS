num_cm = int(input())  # Chicken menu –  10.35 BGN
num_fm = int(input())  # Fish menu - 12.40 BGN
num_vm = int(input())  # Vegan menu - 8.15 BGN
menus_sum = (num_cm * 10.35) + (num_fm * 12.40) + (num_vm * 8.15)
desert = menus_sum * 0.2
total_price = menus_sum + desert + 2.50  # delivery fee is 2.50
print(total_price)
