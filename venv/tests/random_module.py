'''
This is to demonstrate the usage of random module
'''

import random

members = ['Shrenik', 'Nihal', 'Saira', 'Michelle', 'Pranav']
for i in range(3):
    print(random.random())
    print(random.randint(10,20))
    print(random.choice(members))




