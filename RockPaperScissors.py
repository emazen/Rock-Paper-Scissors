# Importing required modules
import random

rps = ["Rock" ,"Paper", "Scissors"]

# Total scores are stored in these variables
user_score = 0
opp_score = 0

# Introduction
print("Rock Paper Scissors !")

print("This game is a best of 3")

print("You will be playing against the computer.")

running = True

# Main game
while running:
    user_input = input("Type Rock, Paper or Scissors: ")
    
    # Printing this just to look more organized
    print("************************************")

    opponent = random.choice(rps)

    if user_input == opponent:
        print("Your opponent picked",opponent)
        print("Its a tie !")
        print("The score is: {} - {}".format(user_score, opp_score))
    if opponent == "Rock":
        if user_input == "Paper":
            print("Your opponent picked",opponent)
            print("Paper beats Rock")
            print("You win !")
            user_score += 1
            print("The score is: {} - {}".format(user_score, opp_score))
        elif user_input == "Scissors":
            print("Your opponent picked",opponent)
            print("Rock beats Scissors")
            print("You lost !")
            opp_score += 1
            print("The score is: {} - {}".format(user_score,opp_score))
    elif opponent == "Paper":
        if user_input == "Rock":
            print("Your opponent picked",opponent)
            print("Paper beats Rock")
            print("You lose !")
            opp_score += 1
            print("The score is: {} - {}".format(user_score, opp_score))
        elif user_input == "Scissors":
            print("Your opponent picked",opponent)
            print("Scissors beat Paper")
            print("You win !")
            user_score += 1
            print("The score is: {} - {}".format(user_score, opp_score))
    else:
        if user_input == "Paper":
            print("Your opponent picked",opponent)
            print("Scissors beat Paper")
            print("You lost !")
            opp_score += 1
            print("The score is: {} - {}".format(user_score, opp_score))
        elif user_input == "Rock":
            print("Your opponent picked",opponent)
            print("Rock beats Scissors")
            print("You win !")
            user_score += 1
            print("The score is: {} - {}".format(user_score, opp_score))
    # If user reaches the winning score of 3
    if user_score == 3:
        print("You won the game !")
        running = False
        print("The game has ended, want to play again ? (y/n)")
        again = input()
        if again == "y":
            running = True
            user_score = 0
            opp_score = 0
        else:
            running = False
            print("Goodbye !")
    # If computer reaches the winning score of 3
    elif opp_score == 3:
        print("You lost the game !")
        running = False
        print("The game has ended, want to play again ? (y/n)")
        again = input()
        if again == "y":
            running = True
            user_score = 0
            opp_score = 0
        else:
            running = False
            print("Goodbye !")



