'''
This is a program to remove duplicate numbers in a list
'''

numbers = [4, 5, 8, 10, 4, 10, 4, 8]
unique_list = []
for number in numbers:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)

