import random
low = 1
high = 50

correct_answer = random.randint(low,high)
user_number = 0
print(correct_answer)

def numberGuser():
    for i in range(0, 5):
        print(f"You have {5 - i} chance left")
        user_number = int(input(f"Guess a number between 1 and 50: "))
        if user_number == correct_answer:
            print("YOU WIN")
            break;
        elif user_number < correct_answer:
            print("Correct answer is greater!")
        elif user_number > correct_answer:
            print("Correct answer is smaller!")
        else:
            print("You have entered invalid number")
        print("*****************************")

    if user_number != correct_answer:
        print("YOU LOSE")

numberGuser()
print("\ngame over\n")
print("1.Play again \n2.Exit")
n = int(input("Enter 1 or 2:\n"))
if n == 1:
    numberGuser()
elif n == 2:
    print("Game Exit")
else:
    print("Enter 1 or 2")