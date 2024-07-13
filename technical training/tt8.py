import sys
sys.setrecursionlimit(15000)

fibDict={0:0,1:1}
def fib(n):
    '''a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    print(a)'''
    if n==0:
        return 0
    elif n==1:
        return n
    else:
        if(n in list(fibDict.keys())):
            return fibDict[n]
        else:
            fibDict[n]=fib(n-1)+fib(n-2)
            return fibDict[n]


print(fib(int(input('enter the number'))))
