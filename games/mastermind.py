import random


def mastermind():
    l = []
    correct_numbers = 0
    correct_positions = 0

    while len(l) < 4:
        i = int(random.random() * 10)
        if i in l:
            continue
        l.append(i)
    # print(l)

    while correct_positions < 4:

        user_list = make_user_list()

        for i in range(4):
            if user_list[i] in l:
                correct_numbers += 1
            if user_list[i] == l[i]:
                correct_positions += 1

        print('\nYou have {} correct guesses at {} correct positions'.format(
            correct_numbers, correct_positions))

        if correct_positions != 4:
            c = 0
            while c != 'y' and c != 'n':
                s = input('\nGuess again? [y/n]: ')
                try:
                    if s != 'y' and s != 'n':
                        print("Not an option.")
                        continue
                    c = s
                except:
                    print("Not an option.")
                    continue

            if c == 'n':
                print("\nThe correct answer was: {}".format(l))
                print("\n*****")
                print("*BYE*")
                print("*****")
                break
            else:
                correct_numbers = 0
                correct_positions = 0

    if correct_positions == 4:
        print("************************************************")
        print('\nYOU WIN\n\nThe correct answer was: {}'.format(l))
        print("************************************************")


def make_user_list():
    user_list = []
    while len(user_list) < 4:
        s = input("\nEnter a number between 0 and 9: ")
        try:
            j = int(s)
            if j in user_list:
                print("\nNumber already guessed")
                continue
            if j < 0 or j > 9:
                print('Number out of bounds.')
                continue
            user_list.append(j)
        except ValueError:
            print('Not a number.')
            continue

    print('\nYour guess is: {}'.format(user_list))
    return user_list

# mastermind()
