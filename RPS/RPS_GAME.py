import random

#Introduction
print("Hello,\nWelcome to my RPS game, here you play the game Rock, Paper Scissors vs the computer.\n");
print("In order to win the computer you must guess a number between 1-3\nwhich each number represents a role in the game\n");
print("1. Rock.\n2. Paper.\n3. Scissors.")

#Create BOT with a random Int and convert it to string
computer_choice = random.randint(1, 3);
if computer_choice == 1:
    computer_answer = "Rock"
elif computer_choice == 2:
    computer_answer = "Paper"
elif computer_choice == 3:
    computer_answer = "Scissors"

#Set player actions and store them as int and str
player_choice = int(input("Enter a number to choose your role:"))
if player_choice == 1:
    player_answer = "Rock"
elif player_choice == 2:
    player_answer = "Paper"
elif player_choice == 3:
    player_answer = "Scissors"

if player_choice == computer_choice:
    print("Tie! you both picked")
    print(player_answer)
elif player_choice == 1 and computer_choice == 2:
    print("The Computer won!")
    #print(computer_answer, "vs", player_answer)
elif player_choice == 2 and computer_choice == 1:
    print("You won!")
   # print(player_answer "vs" computer_answer)
elif player_choice == 3 and computer_choice == 1:
  print("The Computer won!")
  #print(player_answer "vs" computer_answer)
