import random

def start():
    alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_cap = alphabet_low.upper()
    numbers = '0123456789'
    simbols = '!@#$%&*()-_=+[]{}/?'
    all = [alphabet_low, alphabet_cap, numbers, simbols]

    print('Bem vindo ao gerador de senhas!')

    def get_info1(warn=False):
        if warn is False:
            info1 = input('Quantos caracteres você quer em sua senha?\n')
        else:
            info1 = input('Digite um número inteiro!\n')
        
        if info1.isnumeric():
            return info1
        else:
            get_info1(True)

    def get_info2(warn=False):
        if warn is False:
            info2 = input('Você quer números na senha? Digite "S" para sim e "N" para não\n')
        else:
            info2 = input('Digite "S" para sim e "N" para não!\n')
        
        if info2.lower() in ('s', 'n'):
            return info2
        else:
            get_info2(True)

    def get_info3(warn=False):
        if warn is False:
            info3 = input('Pra finalizar, você deseja caracteres especiais nela? Digite "S" para sim e "N" para não\n')
        else:
            info3 = input('Digite "S" para sim e "N" para não!\n')
        
        if info3.lower() in ('s', 'n'):
            return info3
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

    repeat = input('Você quer repetir? Se sim, digite "S"\n')
    if repeat.lower() == 's':
        start()

while True():
    start()
    input('Do you whant to restart? Press Enter to "Yes"') 
