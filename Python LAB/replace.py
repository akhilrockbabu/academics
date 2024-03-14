a=input("Enter a string : ")
b=a.replace(a[-1],'$')
p=b[0:-1]+a[-1]
print(p)
