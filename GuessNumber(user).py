import random

print('***Welcome to Guess the number!***')

def guess_number():
    low = 1
    high = 100
    number = random.randint(low, high)
    attempts = 0

    while True:
        if low == high:
            break
        guess = int(input(f'Guess a number between {low} and {high}: '))
        attempts += 1
        if guess == number:
            break
        elif guess < number:
            print('Too low!')
            if low < guess:
                low = guess + 1
        elif guess > number:
            print('Too high!')
            if high > guess:
                high = guess - 1
    return number, attempts

playing = True
while playing:
    number, attempts = guess_number()
    print(f'Congratulations! You correctly guessed the number <{number}> with {attempts} attempts.')
    playing = input('Would you like to play again? (y/n): ').lower() == 'y'
    print('******************************')

print('Thanks for playing!')