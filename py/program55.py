#find the no of lines in a file

f=False

try:
    f=open('55.txt','r')
    f.seek(0,0)
    print('no of lines is:',len(f.readlines()))

except IOError as io:
    print(io)

finally:
    if f:
        f.close()
        
    
