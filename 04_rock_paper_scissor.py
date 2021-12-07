"""

*   File                  :       04_rock_paper_scissor.py
*   Description           :       Program to create a simple game of rock, paper and scissor
*   Creator               :       Akash Vijay
*   Date                  :       December 7, 2021

"""

import random

print("\n!! Welcome to Rock, Paper & Scissor !!\n")

choice = int(input("What do you want to choose? 1 for Rock, 2 for Paper and 3 for Scissor: "))
ai_choice = random.randint(1,3)

if choice == 1:
    print("Your choice is Rock.")
    if ai_choice == 1:
        print("Computers' choice is also Rock. It's a draw.")
    elif ai_choice == 2:
        print("Computers' choice is Paper. You lose.")
    elif ai_choice == 3:
        print("Computers' choice is Scissor. You Won.")

elif choice == 2:
    print("Your choice is Paper.")
    if ai_choice == 1:
        print("Computers' choice is Rock. You Won.")
    elif ai_choice == 2:
        print("Computers' choice is Paper. It's a draw.")
    elif ai_choice == 3:
        print("Computers' choice is Scissor. You lose.")

elif choice == 3:
    print("Your choice is Scissor.")
    if ai_choice == 1:
        print("Computers' choice is Rock. You lose.")
    elif ai_choice == 2:
        print("Computers' choice is Paper. You Won.")
    elif ai_choice == 3:
        print("Computers' choice is Scissor. It's a draw.")

else:
    print("Invalid input")