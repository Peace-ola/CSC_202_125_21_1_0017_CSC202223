#DATATYPES

#STRING Printing out individual characters
print("Hello"[4])

#INTEGERS
print(123 + 456)

#FLOAT/DECIMAL NUMBERS
print(3.15469)

#Boolean
True
False

#DATATYPE CONVERSION
name = len(input("what is your name"))
new_name = str(name)
print("Your name has " + new_name + "characters")

#Adding the first digit to the second digit
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = second_digit + first_digit
print(two_digit_number)

#Mathematical operations NB(Double ** is used to raise a number to that power)
9 + 3
9 - 3
9 * 3
9 / 3
9 ** 2
3 * 2 + 3 / 4 - 2

#calculating BMI
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
calc = int(weight) / float(height) **2
calc_as_int = int(calc) # converting floating numbers to integers(whole numbers)
print(calc_as_int)

#Rounding up numbers and to the number of places it places it should be be rounded up to
print(round(7 / 4, 3))

print(8 // 5) #floor division(it divides it as an integer that is a whole number)

#f-string
score = 1
height = 1.56
weight = 76
isWinnings = True

print(f"your score is {score}, your height is {height}, your weight is {weight}, you are winning is {isWinning}")

#calculating months weeks amd days left if you are to live up until 90
age = input =("what is your age?")
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"you have {days_remaining} days, {month_remaining}months, {years_remaining} years remaining")

#calculating months weeks and days left if you are to live up until 90
age = input("what is your age")
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"you have {days_remaining} days, {months_remaining} months, {years_remaining} years remaining")


#building a tip calculator 
print("Welcome to the tip calculator")
price = float(input("what is the total bill? $"))
tip = int(input("what percentage of tip would you like to give? 10, 12, 25?"))
people = int(input("How many people to split the bill?"))
price_with_tip / 100 * price + price
print(price_with_the_tip)
