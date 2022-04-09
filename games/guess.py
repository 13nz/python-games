import random


def guess():
    num = int(random.random() * 101 + 1)
    counter = 0

    while(counter < 8):
        guess = -1
        while guess <= 0:
            s = input("Take a guess: ")
            try:
                g = int(s)
                if g <= 0 or g > 100:
                    print("Number out of bounds.")
                    continue
            except ValueError:
                print('Not a number.')
                continue
            guess = g

        if guess != num:
            if guess < num:
                print("Too low.")
            else:
                print("Too high.")
        else:
            print("\n***********")
            print("* YOU WIN *")
            print("***********")
            break
        counter += 1

        if counter == 8:
            print("\n------------")
            print("| YOU LOSE |")
            print("------------")
