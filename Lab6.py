#Lab 6

def encode(original):  # Code to shift values by three
    new = ''
    for i in original:
        i = int(i) + 3
        if i >= 10:  # if the value exceeds 10 (becomes a 2 digit number) take it down
            i -= 10  # i.e. 10 -> 0
        new += str(i)  # puts everything back nice and tidy
    return new

if __name__ == '__main__':
    while True:
        opt = int(input('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\nPlease enter an option: '))
    
        if opt == 3:  # I like putting exit code first so it's the least cost intensive thing to do
            break
        elif opt == 1:  # defines original password, encodes and defines encoded password, prints confirmation
            original = input('Please enter your password to encode: ')
            encoded = encode(original)
            print('Your password has been encoded and stored!')
        elif opt == 2:  # prints encoded and original password
            print(f'The encoded password is {encoded}, and the original passworded is {original}.')
