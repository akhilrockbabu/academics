import time
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("enter a number"))
start=time.time()
print(fibo(n))
end=time.time()-start
print(end)
