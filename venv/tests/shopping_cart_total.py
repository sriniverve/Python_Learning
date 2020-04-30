'''
This is an example program to calculate total of the shopping car
'''

prices = [1245, 6736, 8728]
total = 0                           #initialize the variable

for price in prices:
    total += price
print('Total amount is {}'.format(total))