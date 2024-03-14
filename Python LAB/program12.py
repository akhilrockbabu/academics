n=input("enter the names seperated with comma")
names=n.split(",")
letter="A"
result=[i for i in names if i[0].lower()==letter.lower()]
print("number of names that start with A are:",len(result))
