import random

def start():
    alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_cap = alphabet_low.upper()
    numbers = '0123456789'
    simbols = '!@#$%&*()-_=+[]{}/?'
    all = [alphabet_low, alphabet_cap, numbers, simbols]

    print('Welcome to password generator!')

    def get_info1(warn=False):
        if warn is False:
            info1 = input('How many digits do you want in your password?\n')
        else:
            info1 = input('Type a valid number!\n')
        
        if info1.isnumeric():
            return info1
        else:
            get_info1(True)

    def get_info2(warn=False):
        if warn is False:
            info2 = input('Do you want numbers in the password? [Y, N]\n')
        else:
            info2 = input('Type "S" for yes or "N" for no!\n')
        
        if info2.lower() in ('y', 'n'):
            return info2.lower()
        else:
            get_info2(True)

    def get_info3(warn=False):
        if warn is False:
            info3 = input('Do your want especial digits on the password? [Y, N]\n')
        else:
            info3 = input('Type "S" for yes or "N" for no!\n')
        
        if info3.lower() in ('y', 'n'):
            return info3.lower()
        else:
            get_info3(True)

    info1 = get_info1()
    info2 = get_info2()
    info3 = get_info3()

    password = ''
    if info2 == 's':
        if info3 == 's':
            for a in range(int(info1)):
                character_type = random.choice(all)
                password += random.choice(character_type)
        else:
            all.pop(3)
            for a in range(int(info1)):
                character_type = random.choice(all)
                password += random.choice(character_type)

    else:
        all.pop(2)
        if info3 == 's':
            for a in range(int(info1)):
                character_type = random.choice(all)
                password += random.choice(character_type)
        else:
            all.pop(2)
            for a in range(int(info1)):
                character_type = random.choice(all)
                password += random.choice(character_type)
        
    print(password)

    repeat = input('Do you want to repeat? [Y]\n')
    if repeat.lower() == 's':
        start()

start()
