'''
This is to demonstrate the usage of inheritance
'''

class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    pass                            #empty class

class Cat(Mammal):
    def meow(self):
        print("Meow")

cat1 = Cat()
cat1.walk()
cat1.meow()