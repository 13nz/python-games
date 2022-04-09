from games.RPGCharacter import RPGCharacter


def rpg():
    c = create_character()
    print(c)
    rolling = True

    while rolling:
        print('\nWould you like to roll?')
        try:
            s = input('[y/n]: ')
            if s != 'y' and s != 'n':
                print('Not an option')
                continue
        except:
            print('Invalid input')
        choice = s

        if choice == 'y':
            rolls = user_roll()
            print('\nYou got: ')
            c.roll(rolls[0], rolls[1])

        if choice == 'n':
            print('\nGame Over')
            rolling = False
            break


def create_character():
    d = dict()
    attr = ['strength', 'intelligence', 'wisdom',
            'charisma', 'dexterity', 'constitution']
    print("\nEnter a number from 1 to 20 to set your character's attributes. Press 0 for random")

    for a in attr:
        while a not in d:
            s = input("What is your character's {}? -> ".format(a))
            try:
                i = int(s)
                if i < 0 or i > 20:
                    print('Number out of bounds')
                    continue
                d[a] = i
            except:
                print('Invalid input')
                continue

    c = RPGCharacter(d['strength'], d['intelligence'], d['wisdom'],
                     d['charisma'], d['dexterity'], d['constitution'])
    return c


def user_roll():
    print('Roll for what?')
    print('\nPress 1 for strength\nPress 2 for intelligence\nPress 3 for wisdom\nPress 4 for charisma\nPress 5 for dexterity\nPress 6 for constitution')
    attr_choice = 0
    attr = 0

    while attr_choice <= 0:
        s = input('\nEnter: ')

        try:
            i = int(s)
            if i <= 0 or i > 6:
                print('Not an option')
                continue
        except:
            print('Invalid input')
        attr_choice = i

    if attr_choice == 1:
        attr = 'strn'
    elif attr_choice == 2:
        attr = 'intel'
    elif attr_choice == 3:
        attr = 'wis'
    elif attr_choice == 4:
        attr = 'cha'
    elif attr_choice == 5:
        attr = 'dex'
    elif attr_choice == 6:
        attr = 'con'

    print('\nSelect a modifier')
    mod = -1

    while mod != '0' and mod != 'a' and mod != 'd':
        s = input('[0/a/d]: ')
        if s != '0' and s != 'a' and s != 'd':
            print('Invalid input')
            continue
        mod = s

    return attr, mod


# rpg()
