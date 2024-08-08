import random


def guess_game():
    guess = 0
    adm_num = random.randint(0, 100)
    usr_num = int(input("Enter a guess: "))
    while adm_num != usr_num:
        if usr_num > adm_num:
            print("Too high!")
            usr_num = int(input("Enter a guess: "))
        elif usr_num < adm_num:
            print("Too low!")
            usr_num = int(input("Enter a guess: "))
        else:
            print("You won!")
            break
        guess += 1
        if guess == 4:  # because guess starts from 0
            print(f"You lost! The number was {adm_num}")
            break
    else:
        print("You won!")


def for_loop_step():
    for i in range(1, 15, 3):  # for loop from 1 to 15 (not including 15) and step 3
        print(i)


def for_loop_list():
    friends = ["Alex", "Bau", "Nik", "Steve", "Niku", "Esteban", "Theo"]
    # for name in ["Alex", "Bau", "Nik", "Steve", "Niku", "Esteban", "Theo"]
    # for name in range(len(friends)):
    #   print(friends[name])
    for name in friends:
        print(name)


def nested_for_loop():
    friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
    for friend in friends:
        for number in [1, 2, 3]:
            print(friend, number)


def party_invitation():
    names = ['john ClEEse', 'Eric IDLE', 'michael']
    names1 = ['graHam chapman', 'TERRY', 'terry jones']
    # names.extend(names1)
    # names += names1
    names = names + names1
    for i in range(2):
        names.append(str(input(f"Add your friend {i+1}.\n")))
    for name in names:
        print(f"{name.title()}! You are invited to the party on Saturday.\n")

party_invitation()
