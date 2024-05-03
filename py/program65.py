'''Create Rectangle class with attributes length and breadth and methods to
find area and perimeter. Compare two Rectangle objects by their area.'''

class Rectangle:
    def __init__(self,l=0,b=0):
        self.l=l
        self.b=b
        self.a=l*b
    def area(self):
        self.a=self.l*self.b
        return self.a
    def perimeter(self):
        p=2*(self.l+self.b)
        return p
    def __eq__(self,other):
        if(self.a==other.a):
            print("same area")
        else:
            print("not same area")

r1=Rectangle(5,10)
r2=Rectangle(50,2)
print('area of r1 = ',r1.area())
print('area of r2 = ',r2.area())
print('perimeter of r1 = ',r1.perimeter())
print('perimeter of r2 = ',r2.perimeter())
r1==r2

'''area of r1 =  50
area of r2 =  100
perimeter of r1 =  30
perimeter of r2 =  104
not same area'''


