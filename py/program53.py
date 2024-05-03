'''Write lambda functions, each to find area of square, rectangle and triangle.'''

square=lambda n:n*n
rec=lambda l,b:l*b
tri=lambda base,h:1/2*base*h

n=int(input('enter the side of square'))
print('area of square=',square(n))

l=int(input('enter the length of rectangle'))
b=int(input('enter the breadth of rectangle'))
print('area of rectangle=',rec(l,b))

base=int(input('enter the base of triangle'))
h=int(input('enter the height of triangle'))
print('area of triangle=',tri(base,h))


'''enter the side of square5
area of square= 25
enter the length of rectangle4
enter the breadth of rectangle3
area of rectangle= 12
enter the base of triangle5
enter the height of triangle10
area of triangle= 25.0'''

