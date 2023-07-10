 # Number Guessing game
import random

print("Welcome to the number Guessing Game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
number = random.randint(1, 100)
# print(number)
chances = 0
times_run = True

if difficulty == "easy":
    chances = 10
elif difficulty == "hard":
    chances = 5


# while times_run:
def check():
    global times_run
    while times_run:
        user_choice = int(input("Make a guess:"))
        global chances
        if user_choice < number:
            print(" Too low")
            chances -= 1
            print(f"you have {chances} attempts remaining")

        elif user_choice > number:
            print("Too high")
            chances -= 1
            print(f"you have {chances} attempts remaining")
        if user_choice == number:
            # times_run=False
            print(f"You won.   The answer was{user_choice}")
            times_run = False
        if chances==0:
            times_run= False


# for i in range(chances):
check()
