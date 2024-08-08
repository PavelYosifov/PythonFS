friends = []
for i in range(0, 5):
    name = input(f"Please enter friend number {i}: ")
    name = name.capitalize()
    friends.append(name)
print(f"So your friends are: {friends}")

sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sale = (int(input("Enter your sales for Sunday: ")))
sales_w2.append(sale)
sales = []
sales.extend(sales_w1)
sales.extend(sales_w2)
# sales = sales_w1 + sales_w2 - Another way of combining 2 lists
best_day = (max(sales)*1.5)
worst_day = (min(sales)*1.5)
total = (sum(sales) * 1.5)
print(sales)
separately = []
for i in range(len(sales)):
    sales[i] = sales[i] * 1.5  # calculate every day sales
    separately.append(sales[i])
print(f"Best day: {best_day} $")
print(f"Worst day: {worst_day} $")
print(f"Separately we made: {separately} $ and in total we made: {total} $.")

friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']
print(" ".join(friends_list))
