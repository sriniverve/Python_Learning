'''
This is an example of class, constructors & attributes
'''

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('I am {}'.format(self.name))

nik = Person('Shrenik')
nik.talk()

nihal = Person('Nihal')
nihal.talk()

