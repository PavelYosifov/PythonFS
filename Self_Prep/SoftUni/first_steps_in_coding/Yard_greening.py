sf = float(input())
sum = sf * 7.61  # the price per square feet is 7.61 bgn
discount = sum * 0.18
total = sum - discount
# print(f"The final price is {total} lv.")
print("The final price is {} lv.".format(total))
# print(f"The discount is: {discount} lv.")
print("The discount is: {} lv.".format(discount))
