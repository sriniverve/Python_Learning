'''
This is to demonstrate the usage of constructors
'''


class Point:
    def __init__(self, x, y):               #this is called constructor
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')

point1 = Point(10,20)                #This is an object
point2 = Point(40,50)

point1.draw()
point1.move()

print(point1.x)
print(point2.x)
