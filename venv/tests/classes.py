'''
This is to demonstrate the usage of classes
'''

class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')

point1 = Point()                #This is an object
point2 = Point()

point1.draw()
point1.move()

point1.x = 10                   #assigning attributes to the objects
point2.x = 20

print(point1.x)
print(point2.x)
