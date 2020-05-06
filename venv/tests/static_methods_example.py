'''
This is to demonstrate static methods
'''
import datetime

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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('srini', 'verve', '1000000')
emp2 = Employee('shrenik', 'srini', '1500000')
emp3 = Employee.fromstring('Nihal-Ghatge-2000000')

my_date = datetime.date(2019, 10, 10)



print(Employee.is_workday(my_date))