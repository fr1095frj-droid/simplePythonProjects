import random

words = ['computer', 'teacher', 'rainbow', 'forest', 'coffee']

def pick_word():
    word = random.choice(words)
    return word

def hint(word):
    hint_word = ['_'] * len(word)
    return hint_word

def show_hangman(mistakes):
    hangman_art = {0: ('+-----+    \n'
                       '|          \n'
                       '|          \n'
                       '|          \n'
                       '|_____'),
                   1: ('+-----+    \n'
                       '|     o    \n'
                       '|          \n'
                       '|          \n'
                       '|_____'),
                   2: ('+-----+    \n'
                       '|     o    \n'
                       '|     |    \n'
                       '|          \n'
                       '|_____'),
                   3: ('+-----+    \n'
                       '|     o    \n'
                       '|    /|    \n'
                       '|          \n'
                       '|_____'),
                   4: ('+-----+    \n'
                       '|     o    \n'
                       '|    /|\\  \n'
                       '|          \n'
                       '|_____'),
                   5: ('+-----+    \n'
                       '|     o    \n'
                       '|    /|\\  \n'
                       '|    /     \n'
                       '|_____'),
                   6: ('+-----+    \n'
                       '|     o    \n'
                       '|    /|\\  \n'
                       '|    / \\  \n'
                       '|_____')}
    print(hangman_art[mistakes])

print('Welcome to Hangman!')

def main():
    word = pick_word()
    mistakes = 0

    word_holder = hint(word)
    print(word_holder)

    while mistakes < 6 or '_' not in word_holder:
        guess = input('Guess a letter: ')
        if guess.lower() == word:
            print('Correct!')
            break
        if guess in word:
            print(f'Alright "{guess}" is in the word!')
            for i in range(len(word)):
                if guess == word[i]:
                    word_holder[i] = guess

        if guess not in word:
            mistakes += 1
            print(f'You only have {6 - mistakes} chances left')
        print(word_holder)

    if mistakes == 6:
        print('Sorry, you lost!')
    else:
        print('You win!')
    show_hangman(mistakes)


if __name__ == '__main__':
    main()