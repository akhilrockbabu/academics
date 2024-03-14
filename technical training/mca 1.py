'''q11
n=int(input('enter'))
print(n%10)'''



'''q2
n=int(input('enter'))
print(n//10)'''



'''q3
n=int(input('enter'))
m=int(input('enter the num to concatinate'))
m1=m
b=0
while m>0:
    n*=10
    m//=10
n+=m1
print(n)'''



'''q4
def leng(n):
    if n<0:
        n*=-1
    b=0
    while n>0:
        n//=10
        b+=1
    return b
n=int(input('enter'))
m=int(input('enter the num to concatinate'))
temp=m
b=1
while m>0:
    m//=10
    n//=10
    b*=10
print((n*b)+temp)'''



'''q5
n=int(input('enter'))
temp,b=n,1
while temp>0:
    temp//=10
    b*=10
b/=10
print(int(n//b))'''




'''q6
n=int(input('enter'))
temp,b=n,1
while temp>0:
    temp//=10
    b*=10
b/=10
print(int(n%b))'''



'''q7
n=int(input('enter'))
m=int(input('enter the num to concatinate'))
temp,b=n,1
while temp>0:
    temp//=10
    b*=10
print((m*b)+n)'''



def q8(n,m):
    flag_m=0
    if n<0:
        n*=-1
        flag_n=1
    if m<0:
        m*=-1
        flag_m=1
    t1=n
    t2=m
    b=1
    while t2>0:
        t2//=10
        t1//=10
        b*=10
        m*=10
    n-=t1*b
    if flag_m==1:
        m*=-1
    print(m)
    return m+n


def q9(n,m):
    def leng(n):
        if n<0:
            n*=-1
        b=0
        while n>0:
            n//=10
            b+=1
        return b

    def zfill(n):
        c=1
        while n>0:
            c*=10
            n-=1
        return c

    flag_n=0
    if n<0:
        n*=-1
        flag_n=1
    if m<0:
        m*=-1
    t1,t2,t5,m1,m2=n,n,n,m,m
    if leng(n)%2==0:
        half=leng(n)/2
        c=0
        while half>0:
            t1//=10
            half-=1
            c+=1
        t1*=zfill(leng(n)/2+leng(m))
        m1*=zfill(leng(n)/2)
        t5=n%zfill(c)
        if flag_n==1:
            return -1*(t1+m1+t5)
        else:
            return t1+m1+t5
    else:
        half=leng(n)//2
        c=0
        t2//=10
        while half>0:
            t1//=10
            t2//=10
            half-=1
            c+=1
        t1*=zfill(leng(n)/2+leng(m)-1)
        t2*=zfill(leng(n)/2+leng(m))
        t3=n%zfill(c)
        t4=n%zfill(c+1)
        m1*=zfill(leng(t3))
        m2*=zfill(leng(t4))
        if flag_n==1:
            return-1*(t1+t3+m1),-1*(t2+t4+m2)
        else:
            return t1+t3+m1,t2+t4+m2

n=int(input('enter'))
m=int(input('enter the num to concatinate'))
print(q8(n,m))
#print(q9(n,m))

        



    
    
    
    





    
    


    


    



