s=input("enter a name")
char=s[0]
s=s.replace(char,"$")
s=char+s[1:]
print('the replaced string is:',s)
