import random

wins = 0
losses = 0
ties = 0

symbols = {'r': '✊', 'p': '✋', 's': '🖖'}

def winner(user, computer):
    status = 'tie'
    if user == 'r':
        if computer == 's':
            status = 'user'
        elif computer == 'p':
            status = 'computer'
    elif user == 'p':
        if computer == 's':
            status = 'computer'
        elif computer == 'r':
            status = 'user'
    elif user == 's':
        if computer == 'r':
            status = 'computer'
        elif computer == 'p':
            status = 'user'

    return status

def play():
    global wins, losses, ties
    user = input('Rock, paper, scissors (r / p / s): ').lower()
    while user not in ['r', 'p', 's']:
        print('choose again!!')
        user = input('Rock, paper, scissors (r / p / s): ').lower()
    computer = random.choice('rps')

    print(f'user: {symbols[user]}')
    print(f'computer: {symbols[computer]}')

    status = winner(user, computer)
    if status == 'user':
        wins += 1
    elif status == 'computer':
        losses += 1
    elif status == 'tie':
        ties += 1

    print(f'user: {wins} | computer: {losses} | ties: {ties}')



playing = True
while playing:
    play()
    playing = input('Do you want to play again? (y/n): ').lower() == 'y'

print('Thanks for playing!')