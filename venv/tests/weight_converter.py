'''
This program is to convert the weight from Kgs to Lbs & vice-versa
'''

import time

weight = int(input('Pleae enter your weight: '))
unit = input('(L)bs or (K)gs: ')

if unit.upper() == 'L':
    weight /= 2.2
    print('Your weight is {}Kgs'.format(weight))
elif unit.upper() == 'K':
    weight *= 2.2
    print('Your weight is {}Lbs'.format(weight))
else:
    print("Unrecognized characters. Can't determine your weight, exiting")
