'''
This is a program to print the letter F using nested for loops
'''

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    eff = ""
    for count in range(x_count):
        eff += 'x'
    print(eff)
