'''
This is to demonstate class methods
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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def fromstring(cls,string_str):
        first, last, pay = string_str.split('-')
        return cls(first, last, pay)

emp1 = Employee('srini', 'verve', '1000000')
emp2 = Employee('shrenik', 'srini', '1500000')
emp3 = Employee.fromstring('Nihal-Ghatge-2000000')

Employee.set_raise_amt(1.05)
print(emp1.pay)
emp1.apply_raise()
print(emp1.raise_amount)

emp2.apply_raise()
print(emp2.raise_amount)

print(emp3.email)
print(Employee.num_of_employees)



