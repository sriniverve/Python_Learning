'''
This program is an example to demostrate input variables & expressions
'''

birth_year = input('What is your year of birth?')       #Take age input from user
age = 2020 - int(birth_year)                            #typecasting needed between different data types
print('Type of age variable is '+str(type(age)))
print('Your age is '+str(age))