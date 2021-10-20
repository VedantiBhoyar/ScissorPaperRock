import random
print("Choose your move.....")
my_action = input("Rock, Paper or Scissors?")
opponent_action = random.choice(["Rock", "Paper", "Scissors"])
print(f"My choice is: {my_action}")
print(f"Opponent Choose: {opponent_action}")
if my_action == opponent_action:
    print(f"Match is tie..... {my_action}")
elif my_action == "Rock":
    if opponent_action =="Scissors":
        print("Rock smashes scissors.. I win!!")
    else:
        print("Opponent Win!! paper covers rock")
elif my_action == "Paper":
    if opponent_action == "Rock":
        print("I win!!! paper covers rock")
    else:
        print("Opponent Win!! scissors cut paper")
elif my_action == "Scissors":
    if opponent_action == "Paper":
        print("I Win!!! Scissors cut paper")
    else:
        print("Opponent Win.. Rock smashes scissors")
