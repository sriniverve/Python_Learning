'''
This is a demonstration of list functions
'''

numbers = [5, 2, 4, 9, 0, 7]

numbers.append(20)
print(numbers)

numbers.insert(3,40)
print(numbers)

numbers.remove(9)
print(numbers)

numbers.pop(3)
print(numbers)

print(numbers.index(2))
print(numbers.index(7))
print(numbers.count(0))
