import random


colors = ['B', 'R', 'Y', 'G', 'W']

def main():
    pallet = random.choices(colors, k=4)
    print(pallet)
    chances = 5

    while chances > 0:
        guess = [x.upper() for x in input(f'Guess a 4 colored pallet from the list {colors}(with spaces): ').split()]

        if not all(color in colors for color in guess):
            print('Guess according to the list')
            continue
        if len(guess) != 4:
            print('Please enter 4 colored pallet')
            continue

        chances -= 1
        if guess == pallet:
            break

        correct_positions = 0
        incorrect_positions = 0
        temp = guess.copy()

        for i in range(4):
            if guess[i] == pallet[i]:
                correct_positions += 1


            elif guess[i] in temp and guess[i] in pallet:
                incorrect_positions += 1
                temp.remove(guess[i])

        print(f'Correct Positions: {correct_positions} | Incorrect Positions: {incorrect_positions}')
        print(f'You have {chances} left!')


    return pallet, chances

main()