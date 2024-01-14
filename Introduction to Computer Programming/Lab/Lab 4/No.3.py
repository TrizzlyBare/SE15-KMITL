import random

while True:
    player = input("Enter a choice scissor (0), rock (1), paper(2), exit(.):")

    possible = ["rock", "paper", "scissor"]

    computer = random.choice(possible)

    if player == ".":
        print("Good Bye.")
        break

    if player.isnumeric() :
        if player in ["0", "1", "2"]:
            if player == "0":
                if computer == "paper":
                    print("The computer is", computer, "You are scissor. You won.")
                elif computer == "scissor":
                    print("The computer is", computer, "It is a draw")
                else:
                    print("The computer is", computer, "You are scissor. You lose.")

            elif player == "1":
                if computer == "scissor":
                    print("The computer is", computer, "You are rock. You won.")
                elif computer == "rock":
                    print("The computer is", computer, "It is a draw")
                else:
                    print("The computer is", computer, "You are rock. You lose.")

            elif player == "2":
                if computer == "rock":
                    print("The computer is", computer, "You are paper. You won.")
                elif computer == "paper":
                    print("The computer is", computer, "It is a draw")
                else:
                    print("The computer is", computer, "You are paper. You lose.")
        else:
            print("Invalid")
    else : 
        print("Invalid")