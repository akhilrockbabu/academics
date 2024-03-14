numbers=input("enter the numbers seperated with space")
numbers=list(map(int,numbers.split(" ")))
print("largest number=",max(numbers))
print("smallest number=",min(numbers))
