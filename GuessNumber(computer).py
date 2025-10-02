import random

print('<<<Welcome to guessing number by computer !!! >>>')

def play():
    low = int(input('Enter the minimum number: '))
    high = int(input('Enter the maximum number: '))
    attempts = 0

    while True:
        while low > high:
            print('Please enter in correct order.')
            low = int(input('Enter the minimum number: '))
            high = int(input('Enter the maximum number: '))
        if low == high:
            guess = low
            break
        guess = random.randint(low, high)
        # guess = random.randint(low, high)
        attempts += 1
        answer = input(f'>> computer guessed {guess}; is it correct, low or high? (c / l / h): ').lower()

        if answer == 'c':
            break
        elif answer == 'l':
            low = guess + 1
        elif answer == 'h':
            high = guess - 1

    return guess, attempts


playing = True
while playing:
    number, attempts = play()
    print(f'Computer correctly guessed the number <{number}> with {attempts} attempts!')
    playing = input('Would you like to play again? (y/n): ').lower() == 'y'
    print('******************************')

print('Thanks for playing!')