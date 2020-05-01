'''
This is a program that simulate rolling a dice
'''

import random


class Dice:
    def __init__(self):
        pass


    def roll(self):
        return random.randint(1,6), random.randint(1,6)


diceRoll = Dice()

for roll_count in range(10):
    print(diceRoll.roll())
