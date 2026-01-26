import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '+', '%', '&', '(', ')', '$', '*']

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

password = []
for char in range(0, letters_count):
    password.append(random.choice(letters))

for char in range(0, symbols_count):
    password.append(random.choice(symbols))

for char in range(0, numbers_count):
    password.append(random.choice(numbers))

random.shuffle(password)

mixpassword = ""
for char in password:
    mixpassword += char

print(f"Your random password is {mixpassword}")