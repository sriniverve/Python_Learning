'''
This is to demonstrate the usage of class variables
'''


class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.num_of_employees += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amount)

emp1 = Employee('srini', 'verve', '1000000')
emp2 = Employee('shrenik', 'srini', '1500000')

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

emp2.raise_amount = 1.05
emp2.apply_raise()
print(emp2.pay)

print(Employee.num_of_employees)


