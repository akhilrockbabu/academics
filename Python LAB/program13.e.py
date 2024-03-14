current=int(input("enter the current year"))
future=int(input("enter the future year"))
result=[year for year in range(current,future) if year%4==0 and (year%400==0 or year%100!=0)]
print("the leap years from",current,"to",future,"are:")
for i in result:
    print(i)
