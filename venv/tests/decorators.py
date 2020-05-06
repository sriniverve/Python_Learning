'''
This is to demonstrate the usage of decorators
'''

import time
import math

#function decorators
def decorator_timer(func):
    #print('came in to the decorator')
    def timer_function(*args, **kwargs):
        print('Inner function started')
        begin_time = time.time()
        print(begin_time)

        func(*args, **kwargs)
        time.sleep(1)
        end_time = time.time()
        print(end_time)
        return (end_time - begin_time)

    return timer_function

@decorator_timer
def factorial_find(number):
    return math.factorial(number)


fac = factorial_find(500)
print(f'factorial of 500 is {fac}')







