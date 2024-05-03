numbers=input("enter the numbers seperated with comma")
numbers=list(map(int,numbers.split(",")))
sort=[]
for i in numbers:
    if min(numbers)==i:
        sort.append(i)
        numbers.remove(i)
print("second samllest number=",sort[1])
        
