'''
This is to demonstrate the usage of parameters in functions
'''

def greet_user(first_name,last_name):
    print('Hi {} {}'.format(first_name,last_name))
    print('Welcome aboard')


print('Start')
greet_user('Shrenik', 'Srini')                                      #positional arguments, order matters
greet_user(last_name='Ghatge',first_name='Nihal')                   #keyword arguments, order does not matter
print('finish')