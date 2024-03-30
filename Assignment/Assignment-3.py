import random
low = 1
high = 50


def restartOrExit():
    print("1.Play again \n2.Exit")
    n = int(input("Enter 1 or 2:\n"))
    if n == 1:
        numberGuser()
    elif n == 2:
        print("Game Exit")
        return
    else:
        print("Invalid! Enter 1 to play again or 2 to exit the Game")
        restartOrExit()

def numberGuser():

    correct_answer = random.randint(low, high)
    print(correct_answer)
    user_number = 0

    for i in range(0, 5):
        print(f"You have {5 - i} chance left")
        user_number = int(input(f"Guess a number between {low} and {high}: "))

        if user_number == correct_answer:
            print("YOU WIN")
            print("\ngame over\n")
            restartOrExit()
            break;
        elif user_number < correct_answer:
            print("Correct answer is greater!")
        elif user_number > correct_answer:
            print("Correct answer is smaller!")
        print("*****************************")


    if user_number != correct_answer:
        print("YOU LOSE")
        print("\ngame over\n")
        restartOrExit()

numberGuser()
