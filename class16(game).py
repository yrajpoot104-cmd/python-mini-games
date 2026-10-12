#Rock Paper game

import random

# 1 - Rock
# 2 - Paper
# 3 - Scissors
com_score = 0
user_score = 0
while True:
    print()
    print()
    print()
    print()
    if user_score == 5:
        print("congratulation you won")
        break
    elif com_score == 5:
        print("sorry computer won")
        break 

    print(f"score = computer - {com_score} , human - {user_score}")
    com = random.randint(1,3)
    print("1 - Rock , 2 - Paper , 3 - scissors ")
    user = int(input("select your option :"))
    if user >= 1 and user <= 3:

        if user == com:
            print("its a draw!")

        elif user == 1 and com == 3:
            print("you won")
            user_score += 1

        elif user == 2 and com == 1:
            print("you won")
            user_score += 1

        elif user == 3 and com == 2:
            print("you won")
            user_score += 1

        else:
            print("computer won !")
            com_score += 1

    else:
        print("are you idiot choose between 1-3")
