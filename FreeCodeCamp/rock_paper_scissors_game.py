import random
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"] # declaring a list of options
    computer_choice=random.choice(options) # creating a random choice for the computer using random
    choices = {"player":player_choice, "computer":computer_choice}
    return choices
def check_win(player, computer):
    # print ("You chose "+ player + ", Computer chose" + computer)
    print (f"You chose {player}, Computer choose {computer}") #f stringpap
    if player == computer:
        return "It's a tie!"
   # elif player == "rock" and computer == "scissors": #using and in if
    elif player == "rock":
        if computer== "scissors":
            return "Rock smashes scissors! You win!"
   # elif player == "rock" and computer == "paper": #using and in if
        else:    
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer== "rock":
            return "Paper covers rock! You win!"
        else:    
            return "Scissors cuts paper! You lose!"
    elif player == "scissors":
        if computer== "paper":
            return "Scissors cuts paper! You win!"
        else:    
            return "Rock smashes scissors! You lose!"   
         
choices = get_choices() 
result = check_win(choices["player"], choices["computer"])
print(result)