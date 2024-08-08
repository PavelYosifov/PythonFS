nylon = int(input())  # nylon price is 1.50
paint = int(input())  # paint price is 14.50
diluent = int(input())  # diluent price is 5
hours = int(input())
nylon_price = (nylon + 2) * 1.50
paint_price = (paint + (paint * 0.1)) * 14.5
diluent_price = diluent * 5
materials = nylon_price + paint_price + diluent_price + 0.4
workers = (materials * 0.3) * hours
total_expenses = workers + materials
print(total_expenses)
