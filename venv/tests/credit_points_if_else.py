'''
This programs is to determin if the buyer has enough credit to buy the house, appropriate discount is applied
'''

house_price = 1000000
is_credit = False

if is_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2

print('Down payment for the house is ${}'.format(down_payment))