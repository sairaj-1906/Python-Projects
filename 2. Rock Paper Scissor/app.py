"""
Workflow of project:
1- Input from user (Rock, Paper, Scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = Tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B- Paper
Paper - Rock = Tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = Tie
Scissor - Paper = Paper win
Scissor - Rock = Scissor win
"""

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move from Rock/Paper/Scissor = ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}")
print(f"Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same,\n MATCH TIE!!")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock. Computer Win!!")
    else:
        print("Rock smashes Scissor. You Win!!")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper. Computer Win!!")
    else:
        print("Paper covers Rock. You Win!!")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor. Computer Win!!")
    else:
        print("Scissor cuts Paper. You Win!!")
