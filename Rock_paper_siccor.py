import random

ch = ["Rock", "Paper", "Scissors"]

# Provide bot choice
def get_bot():
    return random.choice(ch)

# Takes choice from user
def get_user_choice():
    user = input("Enter your Choice [Rock | Paper | Scissors] or type 'exit' to quit: ").capitalize()
    if user.lower() == 'exit':
        return 'exit'
    while user not in ch:
        user = input("Invalid Choice. Enter [Rock | Paper | Scissors] or type 'exit' to quit: ").capitalize()
        if user.lower() == 'exit':
            return 'exit'
    return user

# Game result
def result(user, bot):
    if user == bot:
        return "It's a tie!!"
    elif user == "Rock" and bot == "Scissors":
        return "You Win!!"
    elif user == "Scissors" and bot == "Paper":
        return "You Win!!"
    elif user == "Paper" and bot == "Rock":
        return "You Win!!"
    elif bot == "Rock" and user == "Scissors":
        return "Computer wins"
    elif bot == "Scissors" and user == "Paper":
        return "Computer wins"
    elif bot == "Paper" and user == "Rock":
        return "Computer wins"

# Game Process
def play():
    while True:
        bot_choice = get_bot()
        user_choice = get_user_choice()
        if user_choice == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        print("\nYou Chose:", user_choice)
        print("Computer Chose:", bot_choice)
        output = result(user_choice, bot_choice)
        print(output)

play()
