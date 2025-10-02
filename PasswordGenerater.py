import string
import random

def generate_password(min_length, number, special):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special:
        characters += special_chars

    has_numbers = False
    has_special = False
    meets_criteria = False

    psw = ''
    while not meets_criteria or len(psw) < min_length:
        new_char = random.choice(characters)
        psw += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special_chars:
            has_special = True

        meets_criteria = True
        if number:
            meets_criteria = meets_criteria and has_numbers
        if special:
            meets_criteria = meets_criteria and has_special

    return psw

min_length = int(input('Enter minimum password length: '))
has_numbers = input('Do you want your password to have numbers? (y/n): ').lower() == 'y'
has_specials = input('Do you want your password to have punctuations? (y/n): ').lower() == 'y'

print(f'You password is: {generate_password(min_length, has_numbers, has_specials)}')
