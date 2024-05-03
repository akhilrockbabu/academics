word="apple"
l=list(word)
result=[i for i in l if i.lower( )=="a" or i.lower( )=="e" or i.lower( )=="i" or i.lower( )=="o" or i.lower( )=="u"]
print("the given word=",word)
print("vowels are:")
for i in result:
    print(i)

