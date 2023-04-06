from random import randint, choice

def generator(value):
    password = ''
    for c in range(value):
        password += choice(characters)

    return password

letter = 'abcdefghijklmnopqrstuvwxyz'
letter_upper = letter.upper()
num = '0123456789'
special_characters = '_!@#$%&'

characters = letter + letter_upper + num + special_characters

while True:

    amont_characters = input('Enter the number of characters: ')

    try:
        amont_characters = int(amont_characters)

    except ValueError:
        print('Incorrect data, try again...')
        continue

    print(f'Your password is: {generator(amont_characters)}')

    exit = input('Press any key to continue or 0 to exit... ')

    if exit == '0':
        print('Finishing...')
        break