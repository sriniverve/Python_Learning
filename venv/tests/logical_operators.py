'''
This is to demonstrate the usage of logical operators
'''

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_good_credit and has_high_income and not has_criminal_record:     #and needs both to be True, or needs at least one to be true
    print('Eligible for loan')
else:
    print('Not eligible for loan')

