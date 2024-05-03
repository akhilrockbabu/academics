'''Create a class Publisher (name). Derive class Book (title, author) from Publisher.
Derive dass Python (price, no_of_pages) from Book. Write a program that displays information
about a Python book. Use base dass constructor invocation and method overriding.'''

class Publisher:
    def __init__(self,name='nil'):
        self.name=name
    def display(self):
        print('Name : ',self.name)

class Book(Publisher):
    def __init__(self,name='nil',title='nil',author='nil'):
        super().__init__(name)
        self.title=title
        self.author=author

    def display(self):
        super().display()
        print('title : ',self.title)
        print('auhtor : ',self.author)

class Python(Book):
    def __init__(self,name='nil',title='nil',author='nil',price=0,nop=0):
        super().__init__(name,title,author)
        self.price=price
        self.nop=nop
        
    def display(self):
        super().display()
        print('price : ',self.price)
        print('no of pages : ',self.nop)

p1=Python('wings of fire','wings','APJ',120,450)
p2=Python('harry potter','harrypotter','JK rawling',170,490)

print('BOOK 1')
p1.display()
print('')
print('BOOK 2')
p2.display()

'''BOOK 1
Name :  wings of fire
title :  wings
auhtor :  APJ
price :  120
no of pages :  450

BOOK 2
Name :  harry potter
title :  harrypotter
auhtor :  JK rawling
price :  170
no of pages :  490'''
        

