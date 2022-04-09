import random


def rock_paper_scissors():
    user_streak = 0
    computer_streak = 0

    stars = "*****************************"
    lines = "--------------------"

    while (user_streak < 2 and computer_streak < 2):
        user_guess = get_user_guess()
        computer_guess = int(random.random() * 3 + 1)
        result = get_win(user_guess, computer_guess)

        print('\n~You chose {}~'.format(get_guess(user_guess)))
        print('~The computer chose {}~\n'.format(get_guess(computer_guess)))

        if result == 0:
            print('\n---\nTie\n---')
            continue
        elif result == 1:
            print(lines)
            print('{} beats {}\nComputer wins'.format(
                get_guess(computer_guess), get_guess(user_guess)))
            print(lines)
            computer_streak += 1
            continue
        elif result == 2:
            print(lines)
            print('{} beats {}\nHuman wins'.format(
                get_guess(user_guess), get_guess(computer_guess)))
            print(lines)
            user_streak += 1
            continue

    if user_streak == 2:
        print(stars)
        print('Congraulations human, you won')
        print(stars)
    if computer_streak == 2:
        print(stars)
        print('The computer beat you')
        print(stars)


def get_guess(num):
    if num == 1:
        return 'Rock'
    elif num == 2:
        return 'Paper'
    elif num == 3:
        return 'Scissors'


def get_win(user, computer):
    if user == computer:
        return 0
    elif user == 1 and computer == 2 or user == 2 and computer == 3 or user == 3 and computer == 1:
        return 1
    else:
        return 2


def get_user_guess():
    user_guess = 0
    print("\nPress 1 for rock\nPress 2 for paper\nPress 3 for scissors")
    while user_guess != 1 and user_guess != 2 and user_guess != 3:
        s = input("\nGo: ")
        try:
            guess = int(s)
            if guess > 3 or guess < 1:
                print("\nNot an option")
                continue
            user_guess = guess
        except:
            print('\nInvalid input.')
    return user_guess

# rock_paper_scissors()
