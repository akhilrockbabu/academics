'''Program to implement check for bracket balancing'''

def balance(s):
    l=[]
    for i in s:
        if i in ['{','[','(']:
            l.append(i)
        else:
            if i==')' and l.pop()!='(':
                return False
            if i=='}' and l.pop()!='{':
                return False
            if i==']' and l.pop()!='[':
                return False
    
    if l==[]:
        return True
    else:
        return False
            
s=input('enter the string')
print(balance(s))
