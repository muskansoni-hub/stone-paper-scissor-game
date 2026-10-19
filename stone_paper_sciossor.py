import random
choices = ["stone","paper","scissors"]
user_score = 0
comp_score = 0
draws = 0

while True:
    user = input("enter ur choice (stone/paper/scissors): ")
    if user == "exit":
        print("thanks for playing !!!")
        break     
    
    if user not in choices:
     print("Invalid choice! Try again.")
     continue


    comp = random.choice(choices)
    print("Computer chose:", comp)

    if user == comp:
        print("its a draw !!!")
        draws+= 1
    elif user =="stone" and comp == "scissors":
        print("you won !!!")
        user_score += 1
    elif user =="paper" and comp == "stone":
        print("you won !!!")
        user_score += 1
    elif user =="scissors" and comp =="paper":
        print("you won !!!")
        user_score += 1
    else:
        print("you lost !!!")
        comp_score += 1
       
       
print("Your score:", user_score)
print("Computer score:", comp_score)
print("Draws:", draws)
