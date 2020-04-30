'''
This is to demonstrate the usage of if construct
'''

temperature = input('Enter temperature:')
is_hot = False
is_cold = False

if int(temperature) > 30:
    is_hot = True
if int(temperature) < 5:
    is_cold = True

if is_hot:
    print('This is a hot day')
elif is_cold:
    print('This ia a cold day')
else:
    print('This is a pleasant day')

print('Enjoy your day')