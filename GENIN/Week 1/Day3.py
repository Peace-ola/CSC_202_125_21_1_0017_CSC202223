# ODD or EVEN

number = int(input("Which number do you want to check:\n"))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
    
#BMI 2.0
print("Welcome to BMI Calculator")

height = float(input("Enter your height in m:\n"))

weight = float(input("Enter your weight in kg:\n"))

bmi = weight / (height * height)

if bmi <= 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi <= 25:
    print("You hae a normal weight")
elif bmi > 25 and bmi <= 30:
    print("You are overweight")
elif bmi > 30 and bmi < 35:
    print("You are obese")
elif bmi > 35:
    print("Damn, You are Critically Obese")

# Pizza Order
print("Welcome to my Pizza Ordering Service")

size = input("What size pizza do you want? S, M, or L\n").lower()

pepperoni = input("Do you want pepperoni? Y or N\n").lower()

extra_cheese = input("Do you want extra cheese? Y or N\n").lower()

bill = 0

if size == "s":
    bill += 15
elif size == "m": 
    bill += 20
elif size == "l":
    bill += 25

if pepperoni == "y" and size == "s":
    bill += 2
elif pepperoni == "y" and size == "m" or "l":
    bill += 3
    
if extra_cheese == "y":
    bill += 1

print(f"We have recieved your order, Your total is {bill}")

# Love Calculator
print("Welcome to love calculator")

name1 = input("What is your name? \n").lower()
name2 = input("What is your name? \n").lower()

name = name1 + name2

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

p1 = t+r+u+e
p2 = l+o+v+e

love_score_str = str(p1) + str(p2)
love_score = int(love_score_str)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, You go together like garri and groundnut")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, You are alright together")
else:
    print(f"Your score is {love_score}")

print(f"Your love percentage is {love_score}")

#Treasure Island
print("Welcome to Treasure Island\nYour mission is to find the treasure")

c1 = input("You are at a crossroad, Do you want to go left or right? ").lower()

if c1 =="left":
    c2 = input("You have arrived at a stream, do you want to swim or wait? ").lower()

    if c2 == "wait":
        c3 = input("You are teleported to a location, in front of you is a red, blue and yellow door, which door do you enter? ").lower()

        if c3 == "yellow":
            print("You found the treasure, wasnt that hard was it😊")

        elif c3 == "red" or "blue":
            print("You fell into a pit of fire, you died")

    else:
        print("You Froze to Death")

else:
    print("You were killed by a tiger"
