#program to remove specific line from a file

f=False

try:
    f=open('54.txt','r+')
    f.seek(0,0)
    print('the file is :\n',f.read())
    n=int(input('enter the line number you want to remove'))
    f.seek(0,0)
    l=f.readlines()
    f.truncate(0)
    for i in range(len(l)):
        if i+1!=n:
            f.seek(0,2)
            f.write(l[i])
    f.seek(0,0)
    print('now the file is\n',f.read())

except IOError as io:
    print(io)

finally:
    if f:
        f.close()
            

'''the file is :
 pbvr
kerala
india
good
albert
frestin
akhil
rockiey




enter the line number you want to remove6
now the file is
 pbvr
kerala
india
good
albert
akhil
rockiey'''
