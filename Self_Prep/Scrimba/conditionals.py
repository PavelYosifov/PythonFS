import getpass


# Defining if statements with boolean values
def weather():
    is_raining = False
    is_cold = False
    print("Good Morning")
    if is_raining and is_cold:
        print("Bring Umbrella and jacket")
    elif is_raining and not (is_cold):
        print("Bring Umbrella")
    elif not (is_raining) and is_cold:
        print("Bring Jacket")
    else:
        print("Shirt is fine!")


def atm():
    tries = 0
    amount = float(input("How much money you would like to withdraw?\n"))
    if amount <= 50:
        print("Purchase approved")
    else:
        while True:
            pin = getpass.getpass("Please enter your pin!\n")
            if len(pin) == 4 and pin.isdigit():
                print("Thank you for the information!")
                break
            else:
                print("Invalid pin! please try again")
                tries += 1
                if tries == 3:
                    print(
                        "You entered your pin unsuccessfully 3 times.\nYour account has been blocked!")
                    break


def calc():

    num1 = float(input())

    while True:
        calc_f = str(input())
        if calc_f == "s":
            print(num1)
            break
        num2 = float(input())
        if calc_f == "+":
            num1 = num1 + num2
            print(num1)
        elif calc_f == "-":
            num1 = num1 - num2
            print(num1)
        elif calc_f == "*":
            num1 = num1 * num2
            print(num1)
        elif calc_f == "/":
            num1 = num1 / num2
            print(num1)
        else:
            print("Invalid operation. Please try again.")


def base_calc():
    # Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
    # Hint: use 3 separate inputs
    # Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
    # formula is: temp in C*9/5 + 32 = temp in f
    mode = input(
        'Enter math operation(+,-,*,/ or f for Celsius to Fahrenheit conversion: ')
    num1 = float(input('Enter first number: '))
    if mode.lower() == 'f':
        print(f'{num1} Celsius is equivalent to {(num1*9/5)+32} fahrenheit')
    else:
        num2 = float(input('Enter second number: '))
        if mode == '+':
            print(f'Answer is: {num1 + num2}')
        elif mode == '-':
            print(f'Answer is: {num1 - num2}')
        elif mode == '*':
            print(f'Answer is: {num1 * num2}')
        elif mode == '/':
            print(f'Answer is: {num1 / num2}')
        else:
            print('Input error!')

atm()