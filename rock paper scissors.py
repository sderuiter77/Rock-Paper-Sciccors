from random import randint

print("Hello! This is a game of rock, paper, scissors")
print("Rock....")
print("Paper....")
print("Scissors.... \n\n\n")

wins_computer = 0
wins_player = 0
final_wins = 3

while True:
    choice_player = input("Choose your pick:  ").lower()
    ran = randint(0,2)
    if ran == 0:
        choice_computer = "rock"
    elif ran == 1:
        choice_computer = "paper"
    else:
        choice_computer = "scissors"

    print(f"The computer chose: {choice_computer}")

    if choice_player == choice_computer:
        print("It's a draw!")

    elif choice_player == "rock":
        if choice_computer == "scissors":
            print("You win!")
            wins_player += 1
        else:
            print("Computer wins!")
            wins_computer += 1

    elif choice_player == "paper":
        if choice_computer == "rock":
            print("You win!")
            wins_player += 1
        else: 
            print("Computer wins!")
            wins_computer += 1

    elif choice_player == "scissors":
        if choice_computer == "paper":
            print("You win!")
            wins_player += 1
        else:
            print("Computer wins!")
            wins_computer += 1

    else:
        print("Enter a valid move...")

    if wins_computer == final_wins or wins_player == final_wins:
        break
    
    else:
        print(f"\n\nSCORE: \nYou: {wins_player} \nComputer: {wins_computer} \nWe play again until someone wins 5 times!\n")

if wins_computer > wins_player:
    print("\n\nThe computer won the match, you lose! HAHA")
elif wins_player > wins_computer:
    print("\n\nYou won the match!, NICE JOB!!")
else:
    print("\n\nWhut happened?? ERROR")
