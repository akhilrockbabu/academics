#copy odd and even lines in a file to another file

f=False
f1=False
f2=False

try:
    f=open('56.txt','r+')
    f1=open('56_1.txt','w+')
    f2=open('56_2.txt','w+')
    f.seek(0,0)
    print(f.read())
    f.seek(0,0)
    l=f.readlines()
    for i in range(len(l)):
        if i%2==0:
            f2.seek(0,2)
            f2.write(l[i])
        else:
            f1.seek(0,2)
            f1.write(l[i])
    f1.seek(0,0)
    f2.seek(0,0)
    print('the even line file is:\n',f1.read())
    print('the odd line file is:\n',f2.read())

except IOError as io:
    print(io)

finally:
    if f and f1 and f2:
        f.close()
        f1.close()
        f2.close()
            
    
'''1
2
3
4
5
6
the even line file is:
 2
4
6
the odd line file is:
 1
3
5'''
