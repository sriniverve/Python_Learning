'''
This is to demonstrate the usage of error handling
'''

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
except ValueError:                          #each error comes with a different error types. You need to either know or
    print('Invalid value')                  #find out using wrong code with more testing ;-)
except ZeroDivisionError:
    print('Zero is not a valid age')
