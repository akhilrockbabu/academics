#to find lengthiest line in a file

f=False

try:
    f=open('5758.txt','r')
    f.seek(0,0)
    print('the file is:\n',f.read())
    f.seek(0,0)
    l=f.readlines()
    l.sort(key=len)
    for i in l:
        if len(i)==len(l[-1]):
            print('lengthiest line is:\n',i)
            
except IOError as io:
    print(io)

finally:
    if f:
        f.close()

'''the file is:
 india is my country
all indian are my brothers
and sisters
I love my country
lengthiest line is:
 all indian are my brothers'''
            
