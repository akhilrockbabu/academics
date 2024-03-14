from graphics import rectangle,circle
from graphics.dgraphics import cuboid,sphere
l=int(input('enter the length of rectangle'))
b=int(input('enter the breadth of rectangle'))
h=b=int(input('enter the height of cuboid'))
rectangle.area(l,b)
rectangle.perimeter(l,b)
cuboid.area(l,b,h)
cuboid.volume(l,b,h)

r=int(input('enter the radius'))
circle.area(r)
circle.perimeter(r)
sphere.area(r)
sphere.volume(r)


'''enter the length of rectangle10
enter the breadth of rectangle10
enter the height of cuboid10
area of rectangle = 100
perimeter of rectangle= 40
area of cuboid=  600
volume of cuboid=  1000
enter the radius1
area of circle=  3.14
perimeter of circle=  6.28
area of sphere=  12.56
volume of sphere=  4.1866666666666665'''


