#Day 8
def greet():
   print("hello")
   print("how do you do janet akin?")
   print("is not the weather nice today?")
greet()
#function that allows for input
def greet_with_name(name):
   print(f"hello{name}")
   print(f"how do you do{name}?")
greet_with_name("janet")
   #funtion with more than one input
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}?")
greet_with("janet akin", "nowhere")
greet_with("nowhere", "janet akin")
greet_with(location="london", name="janet")



#final project
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o',
            'p','q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p','q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']
direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))
#create a funtion calle 'encrypt
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)
#create a funtion to 'decode'
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"he decoded text is {plain_text}")
if direction == "encoded":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)



