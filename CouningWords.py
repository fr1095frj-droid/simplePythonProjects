from collections import Counter
import os

def count_words():
    file = input("Please Enter file address(with name and extension): ")
    file_address = ''
    for char in file:
        if char == '\\':
            char = '/'
        file_address += char

    if not os.exists(file_address):
        print("File does not exist")

    content = ''
    with open(file_address, 'r') as f:
        content = f.read()
    words_dict = Counter(content.split())

    print(f'{"word":<7}{"count":>7}')
    for word, count in sorted(words_dict.items()):
        print(f'{word:<7}{count:>7}')

    print(f'%%%% number of unique words: {len(words_dict)}')
    print(f'%%%% number of total words: {sum(words_dict.values())}')

count_words()
