
import random

#banker roulette
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_raw = input("Please enter your names")
names = names_raw.split(", ")

amount = len(names)

choice = random.randint(0, amount-1)
pay = names[choice]

pay = random.choice(names)
print(f"Congrats {pay} will be paying today")

row1 = ["#", "#", "#"]
row2 = ["#", "#", "#"]
row3 = ["#", "#", "#"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to hide your treasure? ")

horizontal = int(position[1])
vertical = int(position[0])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "x"

print(f"{row1}\n{row2}\n{row3}")

# Rock Paper Scissors
print("Welcome to rock paper scissors")

player_choice = input("Type 0 for rock, 1 for paper or 2 for scissors")
computer = random.randint(0,2)

if player_choice == computer:
    print("Its a Draw")
elif player_choice == 0 and computer == 1:
    print("You lose")
elif player_choice == 0 and computer == 2:
    print("You win")
elif player_choice == 1 and computer == 0:
    print("You win")
elif player_choice == 1 and computer == 2:
    print("You lose")
elif player_choice == 2 and computer == 0:
    print("You lose")
elif player_choice == 2 and computer == 1:
    print("You win")
