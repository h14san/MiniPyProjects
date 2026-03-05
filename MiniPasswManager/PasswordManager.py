import string
import random

def get_input(input_text):
    while True:
        try:
            num = int(input(input_text))
            return num
        except ValueError:
            print("Invalid Input")
def password_generator(min_length):
    characters = string.ascii_letters + string.digits + string. punctuation
    password = ""
    for i in range(min_length):
        password += random.choice(characters)
    return password
while True:
    length = get_input("Choose number of characters for your password- ")
    if length >= 12:
        print(f"The Password Generated is; {password_generator(length)}")
        break
    else:
        print(f"{length} characters is too short for a strong password, we suggest you choose at least 12 characters")