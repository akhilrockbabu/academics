n=int(input("enter the limit of numbers"))
a=[]
for i in range(n):
    num=int(input("enter the number"))
    a.append(num)
for i in range(n-1):
    if n==1:
        print("strongest neighbour of",a[i],"= ",a[i+1])
    else:
        if a[i-1]>a[i+1]:
            print("Strongest neighbour of",a[i],"= ",a[i-1])
        else:
            print("Strongest neighbour of",a[i],"= ",a[i+1])
print("Strongest neighbour of",a[n-1],"= ",a[n-2])
            
        
