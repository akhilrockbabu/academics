class Book:
    def __init__(self,title='null',author='null',no_of_pages=0):
        self.title=title
        self.author=author
        self.no_of_pages=no_of_pages

    def setbook(self,title='unknown',author='unknown',no_of_pages=0):
        self.title=title
        self.author=author
        self.no_of_pages=no_of_pages

    def showbook(self):
        return self.title,self.author,self.no_of_pages

b1=Book()
b1.setbook('harrypotter','jk rawling',165)
print('book 1:',b1.showbook())
b2=Book()
b2.setbook('Alice in Wonderland','Lewis Carrol',456)
print('book 2:',b2.showbook())
        
'''book 1: ('harrypotter', 'jk rawling', 165)
book 2: ('Alice in Wonderland', 'Lewis Carrol', 456)'''
