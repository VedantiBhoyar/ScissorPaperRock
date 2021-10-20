import random
name = input("Enter your name to play the game: ")
print(name," get ready to play")
print("Choose your move.....")
user_action = input("Rock, Paper or Scissors?")
computer_action = random.choice(["Rock", "Paper", "Scissors"])
print(f"My choice is: {user_action}")
print(f"Computer choice is : {computer_action}")
if user_action == computer_action:
    print(f"Match is tie..... {user_action}")
elif user_action == "Rock":
    if computer_action =="Scissors":
        print(name," wins!!!!!!!!")
    else:
        print("Computer wins!!!!!!!!")
elif user_action == "Paper":
    if computer_action == "Rock":
        print(name," wins!!!!!!!!")
    else:
        print("Computer wins!!!!!!!!")
elif user_action == "Scissors":
    if computer_action == "Paper":
        print(name,"wins!!!!!!!!")
    else:
        print("Computer wins!!!!!!!!")
