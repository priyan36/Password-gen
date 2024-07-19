import random
import string

def generate_password(min_length, numbers=True, spsl_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if spsl_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if spsl_char:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length : "))
has_number = input("Do you want numbers in password? Y/N : ").lower() == "y"
has_special = input("Do you want special characters in password? Y/N : ").lower()=="y"
pwd = generate_password(min_length,has_number,has_special)
print("Print the generated password is : ",pwd)
