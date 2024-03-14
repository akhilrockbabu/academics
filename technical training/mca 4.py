'''n=int(input('number?'))
for i in range(n):
    for j in range(n):
        if i+j==n//2 or i-j==-(n//2) or i-j==n//2 or i+j==3*(n//2)):
            print('*',end='')
        else:
            print(end=' ')
    print()'''

  
                
                
                
'''n=int(input('number?'))
for i in range(n):
    for j in range(n):
        if i+j>=n//2 and i-j>=-(n//2) and i-j<=n//2 and i+j<=3*(n//2):
            print('*',end='')
        else:
            print(end=' ')
    print()'''

'''n=int(input('number?'))
for i in range(n):
    for j in range(n):
        if (i+j>=n-1 and j<=n//4) or (i>=3*n//4 and j>=n//2 and i+j<=3*(n//2)):
            print('*',end='')
        else:
            print(end=' ')
    print()'''

