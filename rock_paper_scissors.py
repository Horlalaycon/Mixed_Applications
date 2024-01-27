# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon

import random


def computer_choice():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    return computer


computer_point = 0
user_point = 0

while True:

    computer_input = computer_choice()
    user_input = input("Choose rock, paper or scissors, (exit to end the program): ")

    print("*-*" * 16)
    print(f"You picked {user_input.lower()} And Computer picked {computer_input}")

    if user_input.lower() == "rock":
        if computer_input == "rock":
            print("===" * 15)
            print("         It's a tie!")
            print("===" * 15)
        elif computer_input == "paper":
            print("===" * 15)
            print("         Computer wins")
            print("===" * 15)
            computer_point += 1

        elif computer_input == "scissors":
            print("===" * 15)
            print("         You win")
            print("===" * 15)
            user_point += 1

    elif user_input.lower() == "paper":
        if computer_input == "rock":
            print("===" * 15)
            print("         Computer win")
            print("===" * 15)
            computer_point += 1

        elif computer_input == "paper":
            print("===" * 15)
            print("         It's a tie!")
            print("===" * 15)

        elif computer_input == "scissors":
            print("===" * 15)
            print("         You win")
            print("===" * 15)
            user_point += 1

    elif user_input.lower() == "scissors":
        if computer_input == "rock":
            print("===" * 15)
            print("         You win!!")
            print("===" * 15)
            user_point += 1

        elif computer_input == "paper":
            print("===" * 15)
            print("         Computer win")
            print("===" * 15)
            computer_point += 1

        elif computer_input == "scissors":
            print("===" * 15)
            print("         It's a tie!")
            print("===" * 15)

    elif user_input.lower() == "exit":
        print("**" * 15)
        print("Game ending...")
        print("==" * 15)
        print(f"User point: {str(user_point)} \nComputer Point: {str(computer_point)}")
        print("==" * 15)
        quit()

    else:
        print("=-" * 15)
        print("Wrong or Invalid input!!!")
        print("=-" * 15)
