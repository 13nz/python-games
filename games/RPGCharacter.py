import random


def rand_int():
    return int(random.random() * 20 + 1)


class RPGCharacter:
    def __init__(self, strn, intel, wis, cha, dex, con):
        if strn != 0:
            self.strn = strn
        else:
            self.strn = rand_int()

        if intel != 0:
            self.intel = intel
        else:
            self.intel = rand_int()

        if wis != 0:
            self.wis = wis
        else:
            self.wis = rand_int()

        if cha != 0:
            self.cha = cha
        else:
            self.cha = rand_int()

        if dex != 0:
            self.dex = dex
        else:
            self.dex = rand_int()

        if con != 0:
            self.con = con
        else:
            self.con = rand_int()

    def __str__(self):
        return '\nStrength: {}\nIntelligence: {}\nWisdom: {}\nCharisma: {}\nDexterity: {}\nConstitution: {}'.format(self.strn, self.intel, self.wis, self.cha, self.dex, self.con)

    def roll(self, attr, m=0):
        if m == 'a':
            num1 = rand_int()
            bonus1 = (getattr(self, attr) - 10) // 2

            num2 = rand_int()
            bonus2 = (getattr(self, attr) - 10) // 2

            if num1 - num2 > 0:
                result = num1 + bonus1
                print(result)
                return result
            else:
                result = num2 + bonus2
                print(result)
                return result

        if m == 'd':
            num1 = rand_int()
            bonus1 = (getattr(self, attr) - 10) // 2

            num2 = rand_int()
            bonus2 = (getattr(self, attr) - 10) // 2

            if num1 - num2 < 0:
                result = num1 + bonus1
                print(result)
                return result
            else:
                result = num2 + bonus2
                print(result)
                return result

        else:
            num = rand_int()
            bonus = (getattr(self, attr) - 10) // 2

            result = num + bonus
            print(result)
            return result
