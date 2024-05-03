#copy one file to another

f1=False
f2=False

try:
    f1=open('59_1.txt','r+')
    f2=open('59_2.txt','r+')
    f1.seek(0,0)
    f2.seek(0,0)
    print('file 1 is:\n',f1.read())
    print('file 2 is:\n',f2.read())
    f2.seek(0,0)
    file2=f2.readlines()
    f1.seek(0,2)
    for i in file2:
        f1.seek(0,2)
        f1.write('\n')
        f1.seek(0,2)
        f1.write(i)
    f1.seek(0,0)
    print('copying file 2 to file 1\n now the file 1 is :\n',f1.read())

except IOError as io:
    print(io)

finally:
    if f1 and f2:
        f1.close()
        f2.close()

'''file 1 is:
 hi
hello
how are you
file 2 is:
 iam fine
copying file 2 to file 1
 now the file 1 is :
 hi
hello
how are you
iam fine'''
