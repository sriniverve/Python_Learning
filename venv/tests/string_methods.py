'''
This program is to demonstrate how to use string methods
'''

course = "Python for beginners"
print(len(course))          #to find the length of the string
print(course.upper())       #to convert the string to Upper case letters
print(course.lower())       #to convert the string to lower case letters
print((course.title()))     #to convert the string to title case

print(course.find('nner'))  #to find the first occurrent of the substring, return the index

print(course.replace('nner', 'noway')) #to replace a substring in the string

print(course)               #none of the above operations will change the original variable.

print('thon' in course)     #to find if the substring in the string. Return boolean

