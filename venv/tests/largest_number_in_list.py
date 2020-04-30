'''
This is a program to find the largest number in the list
'''

numbers = [1, 8, 3, 9, 6]
largest = numbers[0]
for number in numbers:
    if number >= largest:
        largest = number
print('Largest number in the list {} is {}'.format(numbers, largest))