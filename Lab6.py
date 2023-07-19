#Lab 6

def encode(original):
    new = ''
    for i in original:
        i = int(i) + 3
        if i >= 10:
            i -= 10
        new += str(i)
    return new


while True:
    opt = int(input('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\nPlease enter an option: '))

    if opt == 3:
        break
    elif opt == 1:
        original = input('Please enter your password to encode: ')
        encoded = encode(original)
        print('Your password has been encoded and stored!')
    elif opt == 2:
        print(f'The encoded password is {encoded}, and the original passworded is {original}.')
