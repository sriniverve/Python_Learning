'''
This program is used to demonstrate the usage of formatted strings
'''

first = 'Shrenik'
last = 'Srinivas'

message = first +'['+last+'] is a python programmer'    #not the right way to do it
print(message)

message = f'{first} [{last}] is a python programmer'
print(message)
message = '{} [{}] is a python programmer'.format(first,last)
print(message)