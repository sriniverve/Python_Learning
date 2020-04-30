'''
This is to demonstrate the usage of conditional operators
'''

temperature = input('Enter the temperature:')

if int(temperature) > 30:
    print('This is a hot day')
elif int(temperature) < 5:
    print('This is a cold day')
else:
    print('This is a pleasant day')