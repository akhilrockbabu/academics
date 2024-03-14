list=[1,2,3,4,5,6,7,8,9]
result=[i for i in list if i%2!=0]
print("the given numbers are:")
for i in list:
    print(i)
print("even removed are:")
for i in result:
    print(i)
