colors=input("enter the name of colours seperated with comma")
result=[]
colors=colors.split(",")
print(colors)
result=[colors[i] for i in range(len(colors)) if i%2!=0]
print(result)
