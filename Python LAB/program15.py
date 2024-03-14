numbers=input("enter numbers seperated with comma")
numbers=list(map(int,numbers.split(",")))
result=[i for i in numbers if i%2==0 and i>0]
print("the given numbers are:")
for i in numbers:
    print(i)
print("the even numbers are:")
for i in result:
    print(i)
