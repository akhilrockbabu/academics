'''to reverse a string using recursion'''

def rev(s):
    if len(s)==1:
        return s[0]
    else:
        return s[-1]+rev(s[:-1])


s=input("enter a string")
print(rev(s))



'''enter a stringAKHIL
LIHKA'''







































    
