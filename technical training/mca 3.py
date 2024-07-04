'''Diagonal
n=int(input('enter the num'))
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')'''


'''Non-diagonal
n=int(input('enter the num'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')'''



'''n=int(input('enter the num'))
for i in range(n+1):
    for j in range(i):
        print('*',end='')
    print('\n')'''


'''n=int(input('enter the num'))
for i in range(n+1):
    for j in range(n,i,-1):
        print('*',end='')
    print('\n')'''



'''n=int(input('enter the num'))
for i in range(0,n):
    for j in range(0,n):
        if j>=i:
            print('*',end='')
        else:
            print(' ',end='')
    print('\n')'''

'''n=int(input('enter the num'))
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print('*',end='')
        else:
            print(end=' ')
    print()'''


'''n=int(input('enter the num'))
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n-1 or i==0 or j==0 or (i==n//2 and j==n//2):
            print('*',end='')
        else:
            print(end=' ')
    print()'''


'''n=int(input('enter the num'))
c=n-1
for i in range(n):
    for j in range((2*n)-1):
        if i+j>=2 and i+j<=c:
            print('*',end='')
        else:
            print(end=' ')
    c+=2
    print()'''


