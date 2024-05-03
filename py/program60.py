#append an existing file with contents accepted from user

f=False

try:
    f=open('60.txt','r+')
    f.seek(0,0)
    print('file  is:\n',f.read())
    ans=input('enter your answer')
    f.seek(0,2)
    f.seek(0,2)
    f.write('\n')
    f.seek(0,2)
    f.write(ans)
    f.seek(0,0)
    print('now the file is :\n',f.read())

except IOError as io:
    print(io)

finally:
    if f:
        f.close()

'''file  is:
 what is your name
enter your answermy name is akhil
now the file is :
 what is your name
my name is akhil'''
