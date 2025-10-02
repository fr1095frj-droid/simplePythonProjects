import random
import time

def spin():
    balance = 100
    rows = random.choices(['🍒', '🍕', '🍋', '🔔', '💵'], k=3)
    return rows

def get_money(rows):
    prize = 0
    prizes = {'🍒': 3, '🍕': 5, '🍋': 7, '🔔': 10, '💵': 25}
    if rows[0] == rows[1] == rows[2]:
        prize = prizes[rows[0]] * 3
    return prize




print('******************************************')
print('Welcome to Py Slot Machine')
print('Symbols are: 🍕, 🍒, 🍋, 🔔, 💵')
print('******************************************')


def main():
    balance = 100
    while balance > 0:

        bet = int(input('How much money would you like to bet? '))
        balance -= bet

        print('Spinning...\n')
        rows = spin()

        for i in range(2):
            print(rows[i], end=' | ')
            time.sleep(1)
        print(rows[-1])
        time.sleep(1)

        prize = get_money(rows)
        if prize > 0:
            print(f'You win! ${prize}')

        balance += prize

        print(f'Your balance is ${balance}')
        print('***********************************')
        order = input('Would you like to play again?(y / n): ')
        if order == 'y':
            continue


main()

