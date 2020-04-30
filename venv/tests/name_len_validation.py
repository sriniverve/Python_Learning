'''
This is an example of validation a string length based on the input given
'''

name = input('Please enter your name:')

if len(name) < 3:
    print('Your name is less than 3 characters long. Min length of the name is 3 characters')
elif len(name) > 50:
    print('Your name is more than 50 characters long. Max length of the name is 50 characters')
else:
    print('You name is {}'.format(name))

