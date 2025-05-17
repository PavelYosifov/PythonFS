fee = int(input())
shoes = fee - (fee * 0.4)  # shoes price is 40% cheaper than the annual fee
kit = shoes - (shoes * 0.2)  # the basketball kit price is 20% cheaper than the shoes
ball = kit * 0.25  # the ball is 1/5 of the kit price
accessories = ball * 0.2  # the accessories are 1/4 of the ball price
expenses = fee + shoes + kit + ball + accessories
print(f'Total expenses for basketball equipment are {expenses}')
