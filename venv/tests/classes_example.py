'''
This is an exmaple of playing with classes
'''

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def full_name(self):
        return f'{self.first} {self.last}'


Emp1 = Employee('srini', 'verve', '1000000')
Emp2 = Employee('shrenik', 'srini', '1500000')

print(Emp2.full_name())


