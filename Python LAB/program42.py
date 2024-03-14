'''program to find fibannocci number'''

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("enter a number"))
print(fibo(n))


'''enter a number5
5'''
