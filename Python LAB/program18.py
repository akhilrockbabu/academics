names=input("enter the names seperated with comma")
n=int(input("enter the number"))
names=list(names.split(","))
for i in names:
    if len(i)>n:
        print(i)
