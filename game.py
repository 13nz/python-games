import games.rpg
import games.guess
import games.mastermind
import games.rock_paper_scissors
import pyfiglet

print('\n')
print(pyfiglet.figlet_format('WELCOME'))

playing = True


def start_game(g):
    if g == 1:
        print(pyfiglet.figlet_format('guessing game'))
        guess.guess()
    elif g == 2:
        print(pyfiglet.figlet_format('rock\npaper\nscissors'))
        rock_paper_scissors.rock_paper_scissors()
    elif g == 3:
        print(pyfiglet.figlet_format('mastermind'))
        mastermind.mastermind()
    elif g == 4:
        print(pyfiglet.figlet_format('R P G'))
        rpg.rpg()


def play_again():
    print("\nPlay again?")
    print("\nPress 1 to play again\nPress 2 to choose a different game\nPress 3 to quit")
    c = 0

    while c <= 0:
        s = input("\nEnter: ")

        try:
            i = int(s)
            if i not in [1, 2, 3]:
                print('Not an option.')
                continue
            c = i
            break
        except:
            print("Invalid input.")
            continue

    return c


while playing:
    g = 0

    while g <= 0:
        print("\nWhat would you like to play?")
        print("\nPress 1 for a guessing game\nPress 2 for rock, paper, scissors\nPress 3 for mastermind\nPress 4 for an RPG\nPress 5 to quit")

        s = input("\nEnter: ")

        try:
            i = int(s)
            if i not in [1, 2, 3, 4, 5]:
                print('Not an option.')
                continue
            g = i
        except:
            print("Invalid input.")
            continue

    if g == 5:
        print(pyfiglet.figlet_format('BYE BYE'))
        playing = False
        break
    else:
        start_game(g)

    while g > 0 and g != 5:
        c = play_again()

        if c == 1:
            start_game(g)
        elif c == 2:
            g = 0
            continue
        elif c == 3:
            print(pyfiglet.figlet_format('BYE BYE'))
            playing = False
            break
