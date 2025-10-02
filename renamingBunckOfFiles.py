import os

def automate_rename():
    address = input('Enter directory path: ')
    general_name = input('Enter a general name for files: ')
    extension = input('Enter extension: ').strip('.')
    path = ''
    for char in address:
        if char == '\\':
            char = '/'
        path += char
    if path[-1] != '/':
        path += '/'


    i = 0
    for file in os.listdir(path):
        file_name = path + file
        new_name = f'{path}{general_name} {i}.{extension}'
        os.rename(file_name, new_name)
        i += 1



automate_rename()

