#copying odd lines of one file to another

f1=False
f2=False

try:
    f1=open('61_1.txt','r+')
    f2=open('61_2.txt','w+')
    f1.seek(0,0)
    print('file 1 is:\n',f1.read())
    f1.seek(0,0)
    file1=f1.readlines()
    for i in range(len(file1)):
        if i%2==0:
            f2.seek(0,2)
            f2.write(file1[i])
    f2.seek(0,0)
    print('odd lines of file 1 in file 2 is:\n',f2.read())

except IOError as io:
    print(io)

finally:
    if f1 and f2:
        f1.close()
        f2.close()

'''file 1 is:
 1
2
3
4
5
6
7
8
9
10
odd lines of file 1 in file 2 is:
 1
3
5
7
9'''
