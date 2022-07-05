import random

def pas_gen():
    letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    digs = '0123456789'
    symbs = '!?@$&._-'
    my_pass = []
    pass_len = int(input('Enter the lenght of password you desired(8 or above): '))
    if pass_len < 8 or type(pass_len) != int:
        print('You entered the wrong lenght. ')
        pass_len = int(input('Enter the lenght of password you desired(8 or above): '))
    for i in range(pass_len // 4):
        my_pass.append(random.choice(digs))
        my_pass.append(random.choice(symbs))
    for i in range(pass_len - len(my_pass) - 1):
        my_pass.append(random.choice(letters.lower()))
    random.shuffle(my_pass)
    password = random.choice(letters.upper()) + ''.join(my_pass)
    print(password)

pas_gen()

