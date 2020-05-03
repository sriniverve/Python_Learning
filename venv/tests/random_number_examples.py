'''
This is to demonstrate pseudorandom numbers
'''

import random
import secrets
import numpy as np

a = random.random()
print(a)

a = random.randint(1,100)
print(a)

mylist = list("ABCDEIFGH")
a = random.choice(mylist)
print(a)

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

print(secrets.randbelow(10))
print(secrets.randbits(10))
print(secrets.choice(mylist))

print(np.random.randint(0,10,[3,4]))