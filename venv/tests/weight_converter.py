'''
This program is to convert the weight from Kgs to Lbs & vice-versa
'''

import time

weight = float(input('Pleae enter your weight: '))
lb_kg = input('(L)bs or (K)gs: ')

if lb_kg == 'l' or lb_kg == 'L':
    weight /= 2.2
    print('Your weight is {}Kgs'.format(weight))
elif lb_kg == 'k' or lb_kg == 'K':
    weight *= 2.2
    print('Your weight is {}Lbs'.format(weight))
else:
    print("Unrecognized characters. Can't determine your weight, exiting")
