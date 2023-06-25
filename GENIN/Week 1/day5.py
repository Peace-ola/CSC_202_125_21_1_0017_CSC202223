#PYTHON LOOPS
#  STUDENT AVERAGE HEIGHT
studheight= input("input a list of students height").split()
for n in range(0, len(studheight)) :
     studheight[n] = int(studheight[n])
print(studheight)
total_heit= 0
for height in studheight :
        total_heit += height
print(total_heit)
num_stud= 0
for students in studheight :
    num_stud +=1
print(num_stud)
avG_height = round(total_heit/num_stud)
print(avG_height)

# STUDENT HIGH SCORE CHALLENGE
studscores= input("input a list of students scores").split()
for n in range(0, len(studscores)):
      studscores[n] = int(studscores[n])
      print(studscores)
higscore =0
for score in studscores :
    #   print(score)
     if score > higscore :
      higscore = score
print(f"the high score is {higscore}")

# ADDING EVEN  NUMBERS CHALLENGE
total = 0
for number in range(1,101) :
    #tieven = number % 2
    # if tieven ==0 :
    if number%2 ==0 :
     total +=number
    print(total)

# FIZZBUZZ CHALLENGE
for number in range(1,101) :
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else :
        print(number)

# PASSWORD GENERATOR
import random
letters =["a","b","c" ,"d" ,"e","f","g" ,"h" ,"i","j","k" ,"l" ,"m","o",
 "p" ,"q" ,"r","s","t" ,"u" ,"v","w","y" ,"z" ,"A","B","C" ,"D" ,"E","F",
"G" ,"H" ,"I","J","K" ,"L" ,"M","N",  "O" ,"P" ,"Q","Z",]
numbers =["1" ,"2" ,"3","4","5" ,"6" ,"7","8","9" ,"0" ]
symbols =["!" ,"#" ,"$","%","&" ,"(" ,")","*","+"]

print("Welcome to the PyPassword generator")
nr_letr=int(input("How many letters would you like in your password \n"))
n_numba=int(input("How many numbers would you like in your password \n"))
n_symbols=int(input("How many symbols would you like in your password \n"))
password = ""
#EAZY LEVEL
# for chr in range(1, nr_letr + 1) :
#  # rand_ch=random.choice(letters)
#   #print(rand_ch)
#   password+= random.choice(letters)
#   #print(password)
# for chr in range(1, n_numba + 1) :
#   password+= random.choice(numbers)
# for chr in range(1, n_symbols + 1) :
#   password+= random.choice(symbols)

# print( f" Your password is {password}")  
#EAZY LEVEL

#HARD LeVeL
password_l=[]

for chr in range(1, nr_letr + 1) :
  password_l.append (random.choice(letters))

for chr in range(1, n_numba + 1) :
  password_l. append (random.choice(numbers))
for chr in range(1, n_symbols + 1) :
  password_l.append (random.choice(symbols))

#print( f" Your password is {password_l}")  
random.shuffle(password_l)
#print( f" Your password is {password_l}")

password=""
for char in password_l :
  password += char
print ( f" Your password is{password}")

# buhk= str(letters[:nr_letr])
# fuki= str(numbers[:n_numba])
# fret= str(symbols[:n_symbols])


        
