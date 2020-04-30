'''
This is a program to print the letter F using nested for loops
'''

f_numbers = [5, 2, 5, 2, 2]
l_numbers = [2, 2, 2, 2, 5]

for x_count in f_numbers:
    eff = ""
    for count in range(x_count):
        eff += 'x'
    print(eff)

for x_count in l_numbers:
    eff = ""
    for count in range(x_count):
        eff += 'x'
    print(eff)