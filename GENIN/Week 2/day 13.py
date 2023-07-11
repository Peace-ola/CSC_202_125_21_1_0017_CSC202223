# Debugging even or odd

num = int(input("Enter a number"))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
# Debugging leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap")
        else:
            print(f"{year} is not leap")
    else:
        print(f"{year} is leap")
else:
    print(f"{year} is not leap")
    
# Debugging FizzBuzz

for i in range(1 ,101):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
